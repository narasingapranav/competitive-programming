class Solution:
    def findCircleNum(self, graph: List[List[int]]) -> int:
        n=len(graph)
        def dfs(graph,va,v):
            va[v]=True
            for i in range(n):
                if graph[v][i]==1 and not va[i]:
                    dfs(graph,va,i)
        cnt=0
        va=[False]*n
        for i in range(n):
            if not va[i]:
                dfs(graph,va,i)
                cnt+=1
        return cnt