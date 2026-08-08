class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q=deque([source])
        vis=set([source])
        while q:
            node=q.popleft()
            if node == destination:
                    return True
            for nei in graph[node]:
                if nei not in vis:
                    vis.add(nei)
                    q.append(nei)
        return False