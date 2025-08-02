import networkx as nx
import matplotlib.pyplot as plt

def draw(graph, shortest_path_edges):
    # Step 1: 建立整張圖
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    # 固定節點位置
    pos = nx.spring_layout(G, seed=42)

    # Step 2: 畫整張圖（灰色邊）
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')
    

    # Step 3: 顯示 Dijkstra 的邊（紅色）
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in shortest_path_edges],
                           edge_color='red', width=3)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.title("Dijkstra Shortest Path Tree")
    plt.show()
