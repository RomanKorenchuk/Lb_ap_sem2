import csv
import math
import networkx as nx
import matplotlib.pyplot as plt
import os

def read_graph(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        graph = []
        for row in reader:
            graph.append([float(x) if float(x) != 0 else math.inf for x in row])
    for i in range(len(graph)):
        graph[i][i] = 0
    return graph

def visualize_graph(graph, mst_edges=None, title="Граф островів"):
    G = nx.Graph()
    N = len(graph)

    for i in range(N):
        G.add_node(i)

    for i in range(N):
        for j in range(i+1, N):
            if graph[i][j] != math.inf:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

    if mst_edges:
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=3, edge_color='green')
        other_edges = [e for e in G.edges() if e not in mst_edges and (e[1], e[0]) not in mst_edges]
        nx.draw_networkx_edges(G, pos, edgelist=other_edges, style='dashed', alpha=0.5)
    else:
        nx.draw_networkx_edges(G, pos)

    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    formatted_edge_labels = {k: f"{v:.1f}" for k, v in edge_labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels, font_color='red')

    plt.title(title)
    plt.axis('off')
    plt.show()

def prim_mst_edges(graph):
    N = len(graph)
    selected = [False] * N
    dist = [math.inf] * N
    parent = [-1] * N
    dist[0] = 0

    for _ in range(N):
        u = -1
        min_dist = math.inf
        for v in range(N):
            if not selected[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        selected[u] = True

        for v in range(N):
            if not selected[v] and graph[u][v] < dist[v]:
                dist[v] = graph[u][v]
                parent[v] = u

    mst_edges = []
    for v in range(1, N):
        if parent[v] != -1:
            mst_edges.append((parent[v], v))
    return mst_edges

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "islands.csv")
    graph = read_graph(csv_path)

    visualize_graph(graph, title="Повний граф островів з відстанями")

    mst_edges = prim_mst_edges(graph)

    visualize_graph(graph, mst_edges=mst_edges, title="Мінімальне остовне дерево (MST)")