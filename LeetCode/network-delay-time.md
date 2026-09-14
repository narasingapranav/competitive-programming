# 🟠 network-delay-time — Network Delay Time

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/network-delay-time/) &nbsp;|&nbsp; **Solved:** 2026-03-02

---

## 📝 Summary

Accepted solution for Network Delay Time on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
