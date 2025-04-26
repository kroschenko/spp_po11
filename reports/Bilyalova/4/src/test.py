import requests
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

CONFIG_FILE = "github_tracker_config.json"
GITHUB_API_URL = "https://api.github.com/repos/{}/releases/latest"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"repositories": {}, "last_check": None}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def get_user_repositories():
    input_str = input("Введите репозитории для отслеживания (через запятую): ")
    repos = [repo.strip() for repo in input_str.split(",") if repo.strip()]
    return repos

def fetch_latest_release(repo):
    url = GITHUB_API_URL.format(repo)
    try:
        response = requests.get(url)
        
        if response.status_code == 404:
            print(f"Репозиторий {repo} не найден или не имеет релизов")
            return None
        elif response.status_code != 200:
            print(f"Ошибка при запросе к API GitHub для {repo}: {response.status_code}")
            return None
        
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения для {repo}: {str(e)}")
        return None

def format_release_info(release):
    return {
        "version": release.get("tag_name", "N/A"),
        "date": release.get("published_at", "N/A")[:10],
        "url": release.get("html_url", "N/A"),
        "changes": release.get("body", "Нет информации об изменениях")
    }

def create_releases_plot(repos_data):
    if not repos_data:
        print("Нет данных для построения графика")
        return
    
    plt.figure(figsize=(12, 6))
    
    for repo, data in repos_data.items():
        if data.get("date") and data["date"] != "N/A":
            try:
                date = datetime.strptime(data["date"], "%Y-%m-%d")
                plt.plot(date, repo, 'o', markersize=10, label=f"{repo} ({data['version']})")
            except ValueError:
                continue
    
    if not plt.gca().has_data():
        print("Недостаточно данных для построения графика")
        return
    
    plt.title("GitHub Releases Timeline")
    plt.xlabel("Release Date")
    plt.ylabel("Repository")
    plt.grid(True, linestyle='--', alpha=0.7)
    
    date_format = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.gcf().autofmt_xdate()
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    
    plt.savefig("github_releases_plot.png", bbox_inches='tight')
    print("\nГрафик сохранен как 'github_releases_plot.png'")
    plt.show()

def check_for_updates(repos):
    config = load_config()
    new_releases = []
    
    for repo in repos:
        print(f"\nПроверяем обновления для {repo}...")
        latest_release = fetch_latest_release(repo)
        
        if not latest_release:
            continue
            
        release_info = format_release_info(latest_release)
        repo_data = config["repositories"].get(repo, {})
        
        if not repo_data or repo_data.get("version") != release_info["version"]:
            print(f"Найден новый релиз: {release_info['version']} ({release_info['date']})")
            print(f"Ссылка: {release_info['url']}")
            print(f"Основные изменения: {release_info['changes'][:200]}...")
            
            config["repositories"][repo] = {
                "version": release_info["version"],
                "date": release_info["date"],
                "url": release_info["url"],
                "last_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            new_releases.append({
                "repo": repo,
                "version": release_info["version"],
                "date": release_info["date"],
                "url": release_info["url"],
                "changes": release_info["changes"]
            })
        else:
            print(f"Новых релизов для {repo} не обнаружено")
    
    config["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_config(config)
    
    create_releases_plot(config["repositories"])
    
    return new_releases

def main():
    print("GitHub Releases Tracker with Visualization")
    print("=" * 50)
    
    repos = get_user_repositories()
    if not repos:
        print("Не указаны репозитории для отслеживания")
        return
    
    new_releases = check_for_updates(repos)
    
    if new_releases:
        print("\nОбнаружены новые релизы:")
        for release in new_releases:
            print(f"- {release['repo']}: {release['version']} ({release['date']})")
    else:
        print("\nНовых релизов не обнаружено")

if __name__ == "__main__":
    main()