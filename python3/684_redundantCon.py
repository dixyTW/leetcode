class UnionFind:
    def __init__(self, N):
        self.parent = [x for x in range(N)]
        self.size = [1 for _ in range(N)]
        
    def union(self,u,v):
        nu, nv = self.find(u), self.find(v)
        if nu == nv:
            return False
        if self.size[nu] > self.size[nv]:
            self.size[nu] += self.size[nv]
            self.parent[nv] = nu
        else:
            self.size[nv] += self.size[nu]
            self.parent[nu] = nv
        return True
        
    def find(self,node):
        if node != self.parent[node]:
            return self.find(self.parent[node])
        else:
            return node
         
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find by rank
        N = len(edges)
        uf = UnionFind(N)
        for u,v in edges:
            if not uf.union(u-1,v-1):
                return [u,v]
        
        #dfs
#         def isConnected(x, y, visited):
#             if x == y:
#                 return True
#             visited.add(x)
#             res = False
#             for node in g[x]:
#                 if node not in visited:
#                     res |= isConnected(node,y,visited)
#             return res
#         g = defaultdict(set)
#         for edge in edges:
#             u, v = edge
#             if isConnected(u,v,set()):
#                 return edge
#             g[u].add(v)
#             g[v].add(u)
            
        
            