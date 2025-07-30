def prim(graph):
    start_node = list(graph.keys())[0]  # 隨機選擇啟始節點
    visited = {start_node}
    edges = []
    
    while len(visited) < len(graph):
        min_edge = None
        for node in visited:
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (node, neighbor, weight)
        
        if min_edge:
            edges.append(min_edge)
            visited.add(min_edge[1])
    
    return edges


if __name__ == '__main__':
    graph = {
    'A': {'B': 4, 'C': 1, 'D': 3},
    'B': {'A': 4, 'D': 2},
    'C': {'A': 1, 'D': 5 , 'E':10},
    'D': {'A': 3, 'B': 2, 'C': 5, 'E': 6},
    'E': {'C':10, 'D': 6}
    }
    prim_result = prim(graph)
    print("Prim 最小生成樹邊：", prim_result)
