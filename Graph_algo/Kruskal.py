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
