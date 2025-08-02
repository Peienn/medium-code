from drawGraph import draw
def DFS(graph, start):
    for neighbor, weight in graph[start].items():
        if neighbor not in visited:
            visited.add(neighbor)
            dfs_edges.append((start, neighbor))  # 記錄走過的邊
            DFS(graph, neighbor)
    return


if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 1, 'D': 3},
        'B': {'A': 4, 'D': 2},
        'C': {'A': 1, 'D': 5 , 'E':10},
        'D': {'A': 3, 'B': 2, 'C': 5, 'E': 6},
        'E': {'C':10, 'D': 6}
    }

    start = 'A'
    visited = set(start)
    dfs_edges = []
    DFS(graph, start)

    print("DFS Traversal:" , [start] + [edges[1] for edges in dfs_edges])        
    draw(graph , dfs_edges)
