import collections
from datetime import datetime

from api import get_github_data
from json_saver import save_data_to_json
from plot import show_plot


def get_github_username() -> str:
    return input("Enter the github username: ")


def get_user_repositories(data: str) -> str:
    return data["data"]["user"]["repositories"]["edges"]


def print_data(commit_dates, sorted_repos, total_commits):
    print(f"Total commits: {total_commits}")
    formatted_dates = [datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%B %Y") for date in commit_dates]
    date_counts = collections.Counter(formatted_dates)
    most_active_month, count = date_counts.most_common(1)[0]
    print(f"Most active month: {most_active_month} ({count} commits)")
    print("TOP 3 repositories by number of commits:")
    for i, (repo_name, commit_count) in enumerate(sorted_repos[:3], 1):
        print(f"{i}. {repo_name} ({commit_count} commits)")


def main():
    username: str = get_github_username()
    repositories: str = get_user_repositories(get_github_data(username))
    save_data_to_json(username, repositories)

    total_commits: int = 0
    commit_dates: list = []
    repo_commits: list = []

    for repository in repositories:
        commits_number: int = int(repository["node"]["defaultBranchRef"]["target"]["history"]["totalCount"])
        total_commits += commits_number
        repo_commits.append((repository["node"]["name"], commits_number))
        for commit in repository["node"]["defaultBranchRef"]["target"]["history"]["edges"]:
            commit_dates.append(commit["node"]["committedDate"])

    sorted_repos = sorted(repo_commits, key=lambda x: x[1], reverse=True)

    print_data(commit_dates, sorted_repos, total_commits)
    show_plot(commit_dates)


if __name__ == "__main__":
    main()
