class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
    def find(self,x):
        if x==self.parent[x]:
            return x
        return self.find(self.parent[x])
    def union(self,x,y):
        pa=self.find(x)
        pb=self.find(y)
        if pa!=pb:
            self.parent[pb]=pa
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=max(max(u,v) for u,v in edges)+1
        uf=UnionFind(n)
        res=[]
        for u,v in edges:
            if uf.find(v)==uf.find(u):
                return [u,v]
            uf.union(u,v)