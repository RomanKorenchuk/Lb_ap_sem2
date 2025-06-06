import os

def read_graph_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    n = int(lines[0])
    graph = [[] for _ in range(n)]

    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        graph[u].append(v)

    return graph, n

def is_root(graph, n, candidate):
    visited = [False] * n
    stack = [candidate]

    while stack:
        node = stack.pop(0)
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    return all(visited)

def find_root_vertex(graph, n):
    for node in range(n):
        if is_root(graph, n, node):
            return node
    return -1

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_path = os.path.join(base_dir, "input.txt")
    output_path = os.path.join(base_dir, "output.txt")

    graph, n = read_graph_from_file(input_path)
    root = find_root_vertex(graph, n)

    with open(output_path, "w") as file:
        file.write(str(root))

if __name__ == "__main__":
    main()