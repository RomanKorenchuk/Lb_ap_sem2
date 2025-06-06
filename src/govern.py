from collections import defaultdict, deque
import os

def find_order(pairs):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_docs = set()

    for after, before in pairs:
        graph[before].append(after)
        in_degree[after] += 1
        all_docs.update([after, before])

    queue = deque([doc for doc in all_docs if in_degree[doc] == 0])
    order = []

    while queue:
        doc = queue.popleft()
        order.append(doc)

        for neighbor in graph[doc]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(all_docs):
        raise ValueError("Цикл у графі — неможливо отримати всі довідки.")

    return order

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    govern_in_path = os.path.join(base_dir, "govern_in.txt")
    govern_out_path = os.path.join(base_dir, "govern.out.txt")

    with open(govern_in_path, "r") as f:
        lines = [line.strip().split() for line in f.readlines()]
    
    order = find_order(lines)

    with open(govern_out_path, "w") as f:
        for doc in order:
            f.write(doc + "\n")

if __name__ == "__main__":
    main()