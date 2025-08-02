from drawGraph import draw

def BFS(graph,start):
    
    
    visited=set(start)
    queue=[start]
    BFS_edges=[]
    
    while queue:
        current_node = queue.pop(0)
        for neighbor, wieght in graph[current_node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                BFS_edges.append( (current_node , neighbor))
                
                
    return BFS_edges


if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 1, 'D': 3},
        'B': {'A': 4, 'D': 2},
        'C': {'A': 1, 'D': 5 , 'E':10},
        'D': {'A': 3, 'B': 2, 'C': 5, 'E': 6},
        'E': {'C':10, 'D': 6}
    }
    
    start='A'
    BFS_edges = BFS(graph,start)
    print("BFS Traversal:" , [start] + [edges[1] for edges in BFS_edges])        
    draw(graph,BFS_edges)
