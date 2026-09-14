# 🟠 number-of-ways-to-arrive-at-destination — Number of Ways to Arrive at Destination

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) &nbsp;|&nbsp; **Solved:** 2026-05-03

---

## 📝 Summary

Accepted solution for Number of Ways to Arrive at Destination on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9 +7
        graph=defaultdict(list)
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        dist=[float('inf')]*n
        ways=[0]*n
        dist[0]=0
        ways[0]=1
        pq=[(0,0)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                if dist[v]>w+d:
                    dist[v]=d+w
                    ways[v]=ways[u]
                    heapq.heappush(pq,(dist[v],v))
                elif dist[v]==d+w:
                    ways[v]=(ways[v]+ways[u] ) % MOD
        return ways[n-1]
```

</details>
