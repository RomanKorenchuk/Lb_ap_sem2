import csv
import math
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

def prim_mst(graph):
    N = len(graph)
    selected = [False] * N
    dist = [math.inf] * N
    dist[0] = 0
    total_weight = 0

    for _ in range(N):
        u = -1
        min_dist = math.inf
        for v in range(N):
            if not selected[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        selected[u] = True
        total_weight += min_dist
        for v in range(N):
            if not selected[v] and graph[u][v] < dist[v]:
                dist[v] = graph[u][v]
    return total_weight


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "islands.csv")

    graph = read_graph(csv_path)
    result = prim_mst(graph)
    print(f"Мінімальна довжина кабелів: {result}")