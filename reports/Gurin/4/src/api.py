from requests import post

from const import GITHUB_API_GRAPHQL_ENDPOINT, GITHUB_TOKEN, QUERY_FILENAME


def get_github_data(username: str) -> str:
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    query: str = load_query_from_file(QUERY_FILENAME)
    variables = {"username": username}
    response = post(GITHUB_API_GRAPHQL_ENDPOINT, headers=headers, json={"query": query, "variables": variables})
    return response.json()


def load_query_from_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
