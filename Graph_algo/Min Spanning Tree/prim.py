import heapq
def prim(graph, start):
    visited = set()
    key = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    key[start] = 0
    heap = [(0, start)]

    while heap:
        k, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u].items():
            if v not in visited and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(heap, (key[v], v))
  
    mst = [(parent[v], v, key[v]) for v in graph if parent[v] is not None]
    total_weight = sum(key[v] for v in graph if parent[v] is not None)
    return total_weight, mst


if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 1, 'D': 3},
        'B': {'A': 4, 'D': 2},
        'C': {'A': 1, 'D': 5 , 'E': 10},
        'D': {'A': 3, 'B': 2, 'C': 5, 'E': 6},
        'E': {'C': 10, 'D': 6}
    }

    total_weight, mst = prim(graph, start='A')

    print("MST total weight:", total_weight)
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} - {v} (weight {w})")
