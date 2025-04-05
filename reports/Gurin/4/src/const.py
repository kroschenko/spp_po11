import os
from dataclasses import dataclass

@dataclass
class MainConst:
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
    GITHUB_API_GRAPHQL_ENDPOINT: str = "https://api.github.com/graphql"
    QUERY_FILENAME: str = "query.graphql"
    JSON_BASE_FILENAME: str = "repositories.json"
