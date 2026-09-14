class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        a=[]
        for (u,v),val in zip(equations,values):
            graph[u].append([v,val])
            graph[v].append([u,1/val])
        n=len(queries)
        def dfs(src,dest,visited,prod):
            if src==dest:
                return prod
            visited.add(src)
            for nei,wei in graph[src]:
                if nei not in visited:
                    ans=dfs(nei,dest,visited,prod*wei)
                    if ans !=-1:
                        return ans
            return -1.0
                     
        res=[]
        for src,dest in queries:
            if src not in graph or dest not in graph:
                res.append(-1.0)
                continue
            else:
                visited=set()
                res.append(dfs(src,dest,visited,1.0))
                continue
        return res