class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        sus=[False]*n
        graph=defaultdict(list)
        for i,j in invocations:
            graph[i].append(j)
        sus[k]=True
        q=deque([k])
        while q:
            no=q.popleft()
            for nei in graph[no]:
                if not sus[nei]:
                    sus[nei]=True
                    q.append(nei)
        for u, v in invocations:
            if not sus[u] and sus[v]:
                return list(range(n))

        return [i for i in range(n) if not sus[i]]