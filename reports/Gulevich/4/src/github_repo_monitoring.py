import json

import requests
from requests.exceptions import RequestException


def get_top_repos(keyword, top_n=10):
    """Get top repositories by keyword from GitHub API."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {"q": keyword, "sort": "stars", "order": "desc", "per_page": top_n}

    try:
        url = "https://api.github.com/search/repositories"
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        repos_data = response.json()["items"][:top_n]
        result = []

        for repo in repos_data:
            repo_info = {
                "name": repo["full_name"],
                "description": repo["description"] or "No description",
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "last_commit": repo["pushed_at"][:10] if repo["pushed_at"] else "N/A",
            }
            result.append(repo_info)

        return result

    except RequestException as ex:
        raise RuntimeError(f"GitHub API request failed: {ex}") from ex


def save_to_json(data, filename="github_top_repos.json"):
    """Save data to JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def print_simple_list(repos, keyword):
    """Print repositories in simple list format."""
    print(f'\nТоп-10 репозиториев по запросу "{keyword}":\n')
    for i, repo in enumerate(repos, 1):
        print(
            f"{i}. {repo['name']} - "
            f"*{repo['stars']:,},    "
            f"{repo['forks']:,} (Last commit: {repo['last_commit']})"
        )


def main():
    """Main function."""
    keyword = input("Введите ключевое слово для поиска репозиториев: ")
    print(f"\nПоиск топ-10 репозиториев по запросу '{keyword}'...")

    try:
        top_repos = get_top_repos(keyword)
        print_simple_list(top_repos, keyword)
        save_to_json(top_repos)
        print("\nРезультаты сохранены в github_top_repos.json")
    except RuntimeError as ex:
        print(f"Ошибка: {ex}")


if __name__ == "__main__":
    main()
