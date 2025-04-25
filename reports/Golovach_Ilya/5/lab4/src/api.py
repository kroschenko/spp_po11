import requests
from const import GITHUB_TOKEN, GITHUB_API_URL


def fetch_github_data(username: str):
    """Fetch GitHub user interaction data including repos, contributions and stars."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

    try:
        user_repos = _fetch_user_repositories(username, headers)
        if not user_repos:
            print("Пользователь не имеет репозиториев.")
            return None

        contributed_prs = _fetch_user_pull_requests(username, headers)
        data = _initialize_data_structure()

        _process_user_repositories(user_repos, username, headers, data)
        _process_contributions(contributed_prs, headers, data)
        _fetch_user_stars(username, headers, data)

        return data

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к GitHub API: {str(e)}")
        return None


def _fetch_user_repositories(username: str, headers: dict) -> list:
    """Fetch all user repositories including forks."""
    url = f"{GITHUB_API_URL}/users/{username}/repos?type=all"
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        print(f"Ошибка при запросе репозиториев: {response.status_code}")
        print(f"Ответ сервера: {response.text}")
        return []

    return response.json()


def _fetch_user_pull_requests(username: str, headers: dict) -> list:
    """Fetch user's pull requests in other repositories."""
    url = f"{GITHUB_API_URL}/search/issues?q=author:{username}+type:pr"
    response = requests.get(url, headers=headers, timeout=10)
    return response.json().get("items", []) if response.status_code == 200 else []


def _initialize_data_structure() -> dict:
    """Initialize the data structure for storing GitHub interactions."""
    return {
        "repos": [],  # Собственные репозитории
        "contributions": [],  # Участие в чужих репозиториях
        "stars": []  # Звёзды
    }


def _process_user_repositories(repos: list, username: str,
                               headers: dict, data: dict) -> None:
    """Process user repositories and collect interaction data."""
    for repo in repos:
        repo_name = repo["full_name"]
        repo_data = {
            "name": repo_name,
            "commits": _fetch_repository_commits(repo_name, username, headers),
            "pull_requests": _fetch_repository_pull_requests(repo_name, headers),
            "issues": _fetch_repository_issues(repo_name, headers)
        }
        data["repos"].append(repo_data)

        if repo.get("fork"):
            _process_forked_repository(repo, repo_name, headers, data)


def _process_forked_repository(repo: dict, repo_name: str,
                               headers: dict, data: dict) -> None:
    """Process forked repository and find pull requests to parent."""
    parent = repo.get("parent")
    if parent:
        parent_repo = parent["full_name"]
        prs = _fetch_pull_requests_from_fork(repo_name, parent_repo, headers)
        if prs:
            data["contributions"].extend(prs)


def _process_contributions(prs: list, headers: dict, data: dict) -> None:
    """Process user contributions to other repositories."""
    for pr in prs:
        repo_url = pr["repository_url"]
        repo_name = "/".join(repo_url.split("/")[-2:])
        pr_data = {
            "repo": repo_name,
            "user": pr["user"]["login"],
            "reviewers": _get_pull_request_reviewers(repo_name, pr["number"], headers)
        }
        data["contributions"].append(pr_data)


def _fetch_user_stars(username: str, headers: dict, data: dict) -> None:
    """Fetch repositories starred by the user."""
    url = f"{GITHUB_API_URL}/users/{username}/starred"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data["stars"] = [repo["owner"]["login"] for repo in response.json()]


def _fetch_repository_commits(repo_name: str, username: str,
                              headers: dict) -> list:
    """Fetch commits for a specific repository."""
    url = f"{GITHUB_API_URL}/repos/{repo_name}/commits?author={username}"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return list({commit["author"]["login"]
                     for commit in response.json()
                     if commit.get("author")})
    return []


def _fetch_repository_pull_requests(repo_name: str, headers: dict) -> list:
    """Fetch pull requests for a specific repository."""
    url = f"{GITHUB_API_URL}/repos/{repo_name}/pulls?state=all"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return [{
            "user": pr["user"]["login"],
            "reviewers": [r["login"] for r in pr.get("requested_reviewers", [])]
        } for pr in response.json()]
    return []


def _fetch_pull_requests_from_fork(fork_name: str,
                                   parent_repo: str,
                                   headers: dict) -> list:
    """Fetch pull requests from a fork to its parent repository."""
    owner, branch = fork_name.split('/')
    url = (f"{GITHUB_API_URL}/repos/{parent_repo}/pulls"
           f"?state=all&head={owner}:{branch}")
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return [{
            "repo": parent_repo,
            "user": pr["user"]["login"],
            "reviewers": _get_pull_request_reviewers(parent_repo, pr["number"], headers)
        } for pr in response.json()]
    return []


def _get_pull_request_reviewers(repo_name: str,
                                pr_number: int,
                                headers: dict) -> list:
    """Fetch reviewers for a specific pull request."""
    url = f"{GITHUB_API_URL}/repos/{repo_name}/pulls/{pr_number}/reviews"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return list({review["user"]["login"]
                     for review in response.json()
                     if review.get("user")})
    return []


def _fetch_repository_issues(repo_name: str, headers: dict) -> list:
    """Fetch issues for a specific repository."""
    url = f"{GITHUB_API_URL}/repos/{repo_name}/issues?state=all"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return list({issue["user"]["login"]
                     for issue in response.json()
                     if issue.get("user")})
    return []


def generate_report(username: str, data: dict, filename: str) -> str:
    """Generate and save a text report of user interactions."""
    report = f"Отчёт по взаимодействиям пользователя {username}:\n\n"

    # Коммиты
    commit_repos = {repo["name"] for repo in data["repos"] if repo["commits"]}
    report += f"Репозитории с коммитами ({len(commit_repos)}):\n"
    report += "\n".join(f"- {repo}" for repo in commit_repos) + "\n\n"

    # Pull Requests
    pr_repos = {repo["name"] for repo in data["repos"] if repo["pull_requests"]}
    pr_repos.update(contrib["repo"] for contrib in data["contributions"])
    report += f"Репозитории с Pull Requests ({len(pr_repos)}):\n"
    report += "\n".join(f"- {repo}" for repo in pr_repos) + "\n\n"

    # Issues
    issue_repos = {repo["name"] for repo in data["repos"] if repo["issues"]}
    report += f"Репозитории с Issues ({len(issue_repos)}):\n"
    report += "\n".join(f"- {repo}" for repo in issue_repos) + "\n\n"

    # Stars
    report += f"Репозитории с звёздами ({len(data['stars'])}):\n"
    report += "\n".join(f"- {owner}" for owner in data["stars"]) + "\n\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    return report
