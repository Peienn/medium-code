def draw(graph, dfs_edges):
    
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    
    # 加入所有邊與權重
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='lightgray', node_size=1000, font_size=14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='blue', width=2)
   
    
    plt.title("DFS Traversal and Tree")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
