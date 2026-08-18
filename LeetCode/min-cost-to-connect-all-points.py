class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        pq=[]
        for i in range(n-1):
            for j in range(i+1,n):
                c=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append((j,c))
                adj[j].append((i,c))
        vis=[False]*n
        res=0
        heapq.heappush(pq,(0,0))
        while pq:
            c,u=heapq.heappop(pq)
            if vis[u]:
                continue
            vis[u]=True
            res+=c
            for b in adj[u]:
                if not vis[b[0]]:
                    heapq.heappush(pq,(b[1],b[0]))
        return res
