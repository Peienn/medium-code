class UF:
    def __init__(self,nodes):
        self.parent = {node:node for node in nodes}
    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        root1 = self.find(u)
        root2 = self.find(v)
        if root1==root2:
            return False
        
        self.parent[root2] = root1
        return True


def krustal(graph):
    edges=[]
    nodes=set()
    total_w=0
    mst=[]
    for node in graph: 
        for neighbor,edge in graph[node].items():
            if (node,neighbor) not in edges:
                edges.append(  (node,neighbor,edge))
            nodes.add(node)
            nodes.add(neighbor)
    edges.sort(key=lambda x:x[2])

    uf = UF(nodes)
    
    for u,v,w in edges:
        
        if uf.union(u,v):
            
            mst.append( (u,v,w))
            total_w +=w            
    
    return mst,total_w





if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 1, 'D': 3},
        'B': {'A': 4, 'D': 2},
        'C': {'A': 1, 'D': 5 , 'E':10},
        'D': {'A': 3, 'B': 2, 'C': 5, 'E': 6},
        'E': {'C':10, 'D': 6}
    }
    mst,total_w = krustal(graph)
    from drawGraph import draw
    draw(graph,mst)
