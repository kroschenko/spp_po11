import json

def save_graph_to_json(graph, filename: str):
    graph_data = {
        "nodes": [{"id": node, "type": graph.nodes[node].get("type", "unknown")} for node in graph.nodes],
        "edges": [{"source": u, "target": v, "type": d["type"]} for u, v, d in graph.edges(data=True)],
    }
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(graph_data, file, ensure_ascii=False, indent=4)
    print(f"Граф сохранён в {filename}")
