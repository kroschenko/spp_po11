import matplotlib.pyplot as plt
import networkx as nx
import requests


# Функция для запроса к GraphQL API GitHub
def query_github_api(username, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    query = """
        query ($username: String!) {
            user(login: $username) {
                contributionsCollection {
                    repositoryContributions(first: 100) {
                        edges {
                            node {
                                repository {
                                    name
                                    owner {
                                        login
                                    }
                                }
                            }
                        }
                    }
                }
                pullRequests(first: 100) {
                    edges {
                        node {
                            repository {
                                name
                                owner {
                                    login
                                }
                            }
                            author {
                                login
                            }
                        }
                    }
                }
                issues(first: 100) {
                    edges {
                        node {
                            repository {
                                name
                                owner {
                                    login
                                }
                            }
                            author {
                                login
                            }
                        }
                    }
                }
                starredRepositories(first: 100) {
                    edges {
                        node {
                            name
                            owner {
                                login
                            }
                        }
                    }
                }
            }
        }
    """

    variables = {"username": username}
    response = requests.post(
        "https://api.github.com/graphql", headers=headers, json={"query": query, "variables": variables}
    )

    return response.json()


# Функция для сбора взаимодействий
def collect_interactions(data):
    interactions = set()

    # Коммиты
    for contribution in data["data"]["user"]["contributionsCollection"]["repositoryContributions"]["edges"]:
        repo = contribution["node"]["repository"]
        interactions.add(repo["owner"]["login"])

    # Pull Requests
    for pr in data["data"]["user"]["pullRequests"]["edges"]:
        repo = pr["node"]["repository"]
        interactions.add(pr["node"]["author"]["login"])
        interactions.add(repo["owner"]["login"])

    # Issues
    for issue in data["data"]["user"]["issues"]["edges"]:
        repo = issue["node"]["repository"]
        interactions.add(issue["node"]["author"]["login"])
        interactions.add(repo["owner"]["login"])

    # Звёзды
    for star in data["data"]["user"]["starredRepositories"]["edges"]:
        repo = star["node"]
        interactions.add(repo["owner"]["login"])

    return interactions


# Функция для построения графа
def build_graph(interactions, username):
    G = nx.Graph()
    G.add_node(username)

    for interaction in interactions:
        G.add_node(interaction)
        G.add_edge(username, interaction)

    return G


# Основная функция
def main():
    username = input("Введите имя пользователя GitHub: ")
    token = input("Введите токен GitHub: ")

    data = query_github_api(username, token)
    interactions = collect_interactions(data)

    print(f"Анализируем взаимодействия пользователя {username}...")
    print(f"Найдено {len(interactions)} связанных разработчиков.")

    G = build_graph(interactions, username)

    # Визуализация графа
    nx.draw(G, with_labels=True)
    plt.savefig("github_network.png")

    # Сохранение графа в JSON
    nx.write_gexf(G, "github_network.gexf")

    print("Граф сохранён в github_network.gexf")
    print("Визуализация графа сохранена в github_network.png")


if __name__ == "__main__":
    main()
