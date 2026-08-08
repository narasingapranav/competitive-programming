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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        id={}
        en={}
        idx=0
        for i in accounts:
            name=i[0]
            for j in i[1:]:
                if j not in id:
                    id[j]=idx
                    idx+=1
                en[j]=name
        uf=UnionFind(idx)
        for i in accounts:
            first=id[i[1]]
            for j in i[2:]:
                uf.union(first,id[j])
        groups={}
        for email in id:
            root=uf.find(id[email])
            if root not in groups:
                groups[root]=[]
            groups[root].append(email)
        ans=[]
        for r,e in groups.items():
            e.sort()
            name=en[e[0]]
            ans.append([name]+e)
        return ans