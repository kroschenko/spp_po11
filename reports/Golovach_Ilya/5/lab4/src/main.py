from api import fetch_github_data, generate_report
from graph_builder import build_interaction_graph
from visualizer import visualize_and_save_graph
from json_saver import save_graph_to_json

def get_github_username() -> str:
    return input("Введите имя пользователя GitHub: ").strip()

def main():
    username = get_github_username()
    print(f"Анализируем взаимодействия пользователя {username}...")

    # Получение данных через API
    repos_data = fetch_github_data(username)
    if not repos_data:
        print("Не удалось получить данные от GitHub API.")
        return

    # Генерация и вывод отчёта
    report = generate_report(username, repos_data, f"{username}_github_report.txt")
    print("\n" + report)
    print(f"\nТекстовый отчёт сохранён в {username}_github_report.txt")

    # Построение графа взаимодействий
    graph = build_interaction_graph(username, repos_data)
    print(f"\nНайдено {len(graph.nodes)-1} связанных разработчика.")

    # Сохранение графа в JSON
    save_graph_to_json(graph, f"{username}_github_network.json")

    # Визуализация графа
    visualize_and_save_graph(graph, f"{username}_github_network.png")

if __name__ == "__main__":
    main()
