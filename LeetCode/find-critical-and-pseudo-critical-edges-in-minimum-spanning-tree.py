from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i in range(len(edges)):
            edges[i].append(i)
        graph = defaultdict(list)
        for u, v, w, idx in edges:
            graph[u].append((v, w, idx))
            graph[v].append((u, w, idx))
        visited = set()
        minheap = [(0, 0)]
        original_mst = 0
        while minheap and len(visited) < n:
            w, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            original_mst += w
            for nei, weight, _ in graph[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (weight, nei))
        critical = []
        pseudo = []
        for u, v, w, idx in edges:
            graph = defaultdict(list)
            for a, b, wt, id2 in edges:
                if id2 == idx:
                    continue
                graph[a].append((b, wt, id2))
                graph[b].append((a, wt, id2))
            visited = set()
            minheap = [(0, 0)]
            mst_weight = 0
            while minheap and len(visited) < n:
                wt, node = heapq.heappop(minheap)
                if node in visited:
                    continue
                visited.add(node)
                mst_weight += wt
                for nei, weight, _ in graph[node]:
                    if nei not in visited:
                        heapq.heappush(minheap, (weight, nei))
            if len(visited) < n or mst_weight > original_mst:
                critical.append(idx)
                continue
            graph = defaultdict(list)
            for a, b, wt, id2 in edges:
                graph[a].append((b, wt, id2))
                graph[b].append((a, wt, id2))
            visited = {u, v}
            mst_weight = w
            minheap = []
            for nei, weight, _ in graph[u]:
                if nei not in visited:
                    heapq.heappush(minheap, (weight, nei))
            for nei, weight, _ in graph[v]:
                if nei not in visited:
                    heapq.heappush(minheap, (weight, nei))
            while minheap and len(visited) < n:
                wt, node = heapq.heappop(minheap)
                if node in visited:
                    continue
                visited.add(node)
                mst_weight += wt
                for nei, weight, _ in graph[node]:
                    if nei not in visited:
                        heapq.heappush(minheap, (weight, nei))
            if len(visited) == n and mst_weight == original_mst:
                pseudo.append(idx)
        return [critical, pseudo]