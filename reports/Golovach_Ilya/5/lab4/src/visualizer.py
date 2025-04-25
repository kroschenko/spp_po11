import matplotlib.pyplot as plt
import networkx as nx

def visualize_and_save_graph(G, filename: str):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)

    # Рисуем узлы
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color="lightblue")
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    # Рисуем рёбра
    edge_labels = nx.get_edge_attributes(G, 'type')
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("GitHub Interaction Network")
    plt.axis("off")
    plt.tight_layout()

    # Сохранение графика
    plt.savefig(filename)
    print(f"Визуализация графа сохранена в {filename}")
    plt.show()
