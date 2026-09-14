class Solution:
    def findCircleNum(self, graph: List[List[int]]) -> int:
        n=len(graph)
        def dfs(graph,vi,v):
            vi[v]=True
            for i in range(n):
                if graph[v][i]==1 and not vi[i]:
                    dfs(graph,vi,i)
        cnt=0
        vi=[False]*n
        for i in range(n):
            if not vi[i]:
                dfs(graph,vi,i)
                cnt+=1
        return cnt