import json
from datetime import datetime

import requests


def get_top_repos(keyword, top_n=10):
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {"q": keyword, "sort": "stars", "order": "desc", "per_page": top_n}

    url = "https://api.github.com/search/repositories"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Ошибка API: {response.status_code}")

    repos_data = response.json()["items"][:top_n]
    result = []

    for repo in repos_data:
        last_commit_date = repo["pushed_at"][:10] if repo["pushed_at"] else "N/A"
        repo_info = {
            "name": repo["full_name"],
            "description": repo["description"] or "No description",
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "last_commit": last_commit_date,
        }
        result.append(repo_info)

    return result


def save_to_json(data, filename="github_top_repos.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def print_simple_list(repos, keyword):
    print(f'\nТоп-10 репозиториев по запросу "{keyword}":\n')
    for i, repo in enumerate(repos, 1):
        print(
            f"{i}. {repo['name']} - "
            f"*{repo['stars']:,},    "
            f"{repo['forks']:,} (Last commit: {repo['last_commit']})"
        )


def main():
    keyword = input("Введите ключевое слово для поиска репозиториев: ")
    print(f"\nПоиск топ-10 репозиториев по запросу '{keyword}'...")

    try:
        top_repos = get_top_repos(keyword)
        print_simple_list(top_repos, keyword)

        save_to_json(top_repos)
        print(f"\nРезультаты сохранены в github_top_repos.json")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
