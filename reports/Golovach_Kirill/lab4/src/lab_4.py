import json
from getpass import getpass
import requests
import matplotlib.pyplot as plt
import pandas as pd
from jinja2 import Environment, FileSystemLoader

# ==== 1. Базовые настройки ====
GITHUB_API_URL = "https://api.github.com"

def get_headers(token=None):
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


# ==== 2. Функции получения данных из GitHub REST API ====

def get_user_repos(username, token):
    repos = []
    page = 1
    while True:
        url = f"{GITHUB_API_URL}/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=get_headers(token))
        if response.status_code != 200 or not response.json():
            break
        repos.extend(response.json())
        page += 1
    return repos


def get_commit_count(username, repo_full_name, token):
    url = f"{GITHUB_API_URL}/repos/{repo_full_name}/commits"
    page = 1
    total_commits = 0
    while True:
        params = {"author": username, "per_page": 100, "page": page}
        response = requests.get(url, headers=get_headers(token), params=params)
        if response.status_code != 200:
            break
        commits = response.json()
        total_commits += len(commits)
        if len(commits) < 100:
            break
        page += 1
    return total_commits


def get_prs(username, repo_full_name, token, state=None):
    url = f"{GITHUB_API_URL}/search/issues"
    query = f"is:pr author:{username} repo:{repo_full_name}"
    if state:
        query += f" state:{state}"
    page = 1
    total = 0
    while True:
        params = {"q": query, "per_page": 100, "page": page}
        response = requests.get(url, headers=get_headers(token), params=params)
        data = response.json()
        total += data.get("total_count", 0)
        items = data.get("items", [])
        if len(items) < 100:
            break
        page += 1
    return total


def get_issues(username, repo_full_name, token):
    url = f"{GITHUB_API_URL}/search/issues"
    query = f"is:issue author:{username} repo:{repo_full_name}"
    page = 1
    total = 0
    while True:
        params = {"q": query, "per_page": 100, "page": page}
        response = requests.get(url, headers=get_headers(token), params=params)
        data = response.json()
        total += data.get("total_count", 0)
        items = data.get("items", [])
        if len(items) < 100:
            break
        page += 1
    return total


# ==== 3. Анализ активности пользователя ====

def analyze_github_user(username, token=None):
    print(f"\nАнализ вклада пользователя: {username}")

    all_repos = get_user_repos(username, token)
    contribution_data = {
        "username": username,
        "repositories": [],
        "total_commits": 0,
        "total_open_prs": 0,
        "total_closed_prs": 0,
        "total_issues": 0,
        "activity_score": 0
    }

    max_activity_repo = {"name": "", "score": 0}

    for repo in all_repos:
        repo_name = repo["full_name"]
        print(f"Обработка репозитория: {repo_name}")

        commits = get_commit_count(username, repo_name, token)
        open_prs = get_prs(username, repo_name, token, state="open")
        closed_prs = get_prs(username, repo_name, token, state="closed")
        issues = get_issues(username, repo_name, token)

        activity = (commits * 1) + (open_prs * 2) + (closed_prs * 3) + (issues * 1.5)

        repo_data = {
            "repository": repo_name,
            "commits": commits,
            "open_prs": open_prs,
            "closed_prs": closed_prs,
            "issues": issues,
            "activity_score": activity
        }

        contribution_data["repositories"].append(repo_data)

        contribution_data["total_commits"] += commits
        contribution_data["total_open_prs"] += open_prs
        contribution_data["total_closed_prs"] += closed_prs
        contribution_data["total_issues"] += issues
        contribution_data["activity_score"] += activity

        if activity > max_activity_repo["score"]:
            max_activity_repo["name"] = repo_name
            max_activity_repo["score"] = activity

    contribution_data["active_repository"] = max_activity_repo

    with open("github_contribution.json", "w", encoding="utf-8") as f:
        json.dump(contribution_data, f, indent=4, ensure_ascii=False)

    return contribution_data


# ==== 4. Визуализация графика активности ====

def visualize_activity(data):
    repos = [item['repository'] for item in data['repositories']]
    activity_scores = [item['activity_score'] for item in data['repositories']]

    df = pd.DataFrame({
        'Репозиторий': repos,
        'Активность': activity_scores
    })

    df = df.sort_values(by='Активность', ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    plt.barh(df['Репозиторий'], df['Активность'], color='skyblue')
    plt.xlabel('Оценка активности')
    plt.title(f'Топ-10 репозиториев ({data["username"]})')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("github_activity_chart.png")
    plt.close()
    print("График активности сохранён как github_activity_chart.png")


# ==== 5. Генерация HTML-отчёта ====

def generate_html_report(data):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")

    repositories = [repo['repository'] for repo in data['repositories']]
    activity_scores = [repo['activity_score'] for repo in data['repositories']]

    rendered = template.render(
        username=data['username'],
        total_commits=data['total_commits'],
        total_open_prs=data['total_open_prs'],
        total_closed_prs=data['total_closed_prs'],
        total_issues=data['total_issues'],
        activity_score=round(data['activity_score'], 2),
        active_repo=data['active_repository']['name'],
        repositories=repositories,
        activity_scores=activity_scores
    )

    with open("github_contribution_report.html", "w", encoding="utf-8") as f:
        f.write(rendered)

    print("HTML-отчет создан как github_contribution_report.html")


# ==== 6. Основная функция запуска ====

def main():
    username = input("Введите имя пользователя GitHub: ")
    use_token = input("Хотите использовать персональный токен? (y/n): ").lower() == 'y'
    token = None
    if use_token:
        token = getpass("Введите ваш GitHub Personal Access Token: ")

    result = analyze_github_user(username, token)

    print(f"\nПользователь {username} внес вклад в {len(result['repositories'])} репозиториев.")
    print(f"Общее количество коммитов: {result['total_commits']}")
    print(f"Открытых pull requests: {result['total_open_prs']}")
    print(f"Закрытых pull requests: {result['total_closed_prs']}")
    print(f"Созданных issues: {result['total_issues']}")
    print(f"Активность: {result['activity_score']:.1f} баллов")
    print(f"Самый активный проект: {result['active_repository']['name']} "
          f"(оценка активности: {result['active_repository']['score']:.1f})")
    print("Результаты сохранены в github_contribution.json")

    visualize_activity(result)
    generate_html_report(result)


# ==== 7. Точка входа ====
if __name__ == "__main__":
    main()
