class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        minheap=[(0,k)]
        dist={}
        while minheap:
            d,node=heapq.heappop(minheap)
            if node in dist:
                continue
            dist[node]=d
            for nei,wei in graph[node]:
                if nei not in dist:
                    heapq.heappush(minheap,(d+wei,nei))
        if len(dist) !=n:
            return -1
        return max(dist.values())