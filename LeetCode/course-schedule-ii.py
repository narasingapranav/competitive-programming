class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        vis={}
        st=[]
        def dfs(node):
            if node in vis:
                if vis[node]==1:
                    return False
                return True
            vis[node]=1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            vis[node]=2
            st.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return st[::-1]