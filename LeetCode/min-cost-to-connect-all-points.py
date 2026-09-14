class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def union(x,y):
            self.parent[x]=y
        def find(x):
            if self.parent[x]==x:
                return x
            return find(self.parent[x])
        n=len(points)
        self.parent=list(range(n))
        p=[0]*n
        for i in range(n):
            p[i]=i
        edges=[[0]*3 for _ in range(n*(n-1)//2)]
        k=0
        res=0
        c=0
        for i in range(n-1):
            for j in range(i+1,n):
                edges[k][0]=i
                edges[k][1]=j
                edges[k][2]=abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1])
                k+=1
        edges.sort(key=lambda x:x[2])
        i=0
        while c<n-1:
            ru=find(edges[i][0])
            rv=find(edges[i][1])
            cost=edges[i][2]
            if ru!=rv:
                res+=cost
                union(ru,rv)
                c+=1
            i+=1
        return res