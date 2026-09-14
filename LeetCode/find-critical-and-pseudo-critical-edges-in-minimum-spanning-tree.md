# 🟠 find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree — Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) &nbsp;|&nbsp; **Solved:** 2026-03-04

---

## 📝 Summary

Accepted solution for Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^12) (estimated -- 12 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`graph` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
