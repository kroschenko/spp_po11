import networkx as nx


def build_interaction_graph(username: str, data: dict) -> nx.Graph:
    """
    Builds an interaction graph for a GitHub user based on their activities.

    Args:
        username: GitHub username
        data: Dictionary containing user's repositories, contributions and stars

    Returns:
        NetworkX Graph object representing user's interactions
    """
    G = nx.Graph()
    G.add_node(username, type="user")

    _add_repository_interactions(G, username, data["repos"])
    _add_contribution_interactions(G, username, data["contributions"])
    _add_star_interactions(G, username, data["stars"])

    return G


def _add_repository_interactions(graph: nx.Graph, username: str, repos: list) -> None:
    """Add interactions from user's own repositories."""
    for repo in repos:
        _add_commit_interactions(graph, username, repo["commits"])
        _add_pull_request_interactions(graph, username, repo["pull_requests"])
        _add_issue_interactions(graph, username, repo["issues"])


def _add_contribution_interactions(graph: nx.Graph, username: str, contributions: list) -> None:
    """Add interactions from contributions to other repositories."""
    for contribution in contributions:
        _add_contribution_edge(graph, username, contribution["user"], "contribution")
        _add_reviewer_edges(graph, username, contribution["reviewers"], "contribution_review")


def _add_star_interactions(graph: nx.Graph, username: str, stars: list) -> None:
    """Add interactions from starred repositories."""
    for owner in stars:
        _add_star_edge(graph, username, owner)


def _add_commit_interactions(graph: nx.Graph, username: str, commits: list) -> None:
    """Add commit interactions to the graph."""
    for author in commits:
        _add_edge_if_valid(graph, username, author, "commit")


def _add_pull_request_interactions(graph: nx.Graph, username: str, pull_requests: list) -> None:
    """Add pull request interactions to the graph."""
    for pr in pull_requests:
        _add_edge_if_valid(graph, username, pr["user"], "pull_request")
        _add_reviewer_edges(graph, username, pr["reviewers"], "pr_review")


def _add_issue_interactions(graph: nx.Graph, username: str, issues: list) -> None:
    """Add issue interactions to the graph."""
    for user in issues:
        _add_edge_if_valid(graph, username, user, "issue")


def _add_reviewer_edges(graph: nx.Graph, username: str, reviewers: list, edge_type: str) -> None:
    """Add reviewer edges to the graph."""
    for reviewer in reviewers:
        _add_edge_if_valid(graph, username, reviewer, edge_type)


def _add_contribution_edge(graph: nx.Graph, username: str, user: str, edge_type: str) -> None:
    """Add a contribution edge to the graph."""
    _add_edge_if_valid(graph, username, user, edge_type)


def _add_star_edge(graph: nx.Graph, username: str, owner: str) -> None:
    """Add a star edge to the graph."""
    _add_edge_if_valid(graph, username, owner, "star")


def _add_edge_if_valid(graph: nx.Graph, source: str, target: str, edge_type: str) -> None:
    """
    Add an edge to the graph if target is valid and not the same as source.

    Args:
        graph: NetworkX Graph to add edge to
        source: Source node
        target: Target node
        edge_type: Type of interaction/edge
    """
    if target and target != source:
        graph.add_edge(source, target, type=edge_type)
