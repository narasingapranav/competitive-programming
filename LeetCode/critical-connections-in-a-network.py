class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        time=1
        def dfs(adj,src,par,vis):
            nonlocal time
            vis[src]=True
            disc[src]=low[src]=time
            time+=1
            for v in adj[src]:
                if v==par:
                    continue
                if vis[v]:
                    low[src]=min(low[src],low[v])
                else:
                    dfs(adj,v,src,vis)
                    low[src]=min(low[src],low[v])
                    if low[v]>disc[src]:
                        res.append((src,v))


        res=[]
        disc=[0]*n
        low=[0]*n
        vis=[False]*n
        adj=defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        dfs(adj,0,-1,vis)
        return res