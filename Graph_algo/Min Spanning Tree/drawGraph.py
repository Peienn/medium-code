# 使用方法(以MST/prim.py舉例):
# 執行完prim之後，得到prim_result
# 再將原圖graph + 得到的prim_result 丟入function即可
# --> draw(graph, prim_result)
import networkx as nx
import matplotlib.pyplot as plt
def draw(graph, other_algorithm):

    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()


    prim_graph = nx.Graph()
    for edge in other_algorithm:
        prim_graph.add_edge(edge[0], edge[1], weight=edge[2])

    #plt.figure(figsize=(10, 5))
    nx.draw(prim_graph, pos, with_labels=True, node_color='lightblue', node_size=2000)
    prim_edge_labels = nx.get_edge_attributes(prim_graph, 'weight')
    nx.draw_networkx_edge_labels(prim_graph, pos, edge_labels=prim_edge_labels)
    plt.show()

