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
    roots = []
    for node in range(n):
        if is_root(graph, n, node):
            roots.append(node)
    return roots

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_path = os.path.join(base_dir, "input.txt")
    output_path = os.path.join(base_dir, "output.txt")

    graph, n = read_graph_from_file(input_path)
    roots = find_root_vertex(graph, n)
    with open(output_path, "w") as file:
        if roots:
            file.write(" ".join(map(str, roots)))
        else:
            file.write("-1")

if __name__ == "__main__":
    main()