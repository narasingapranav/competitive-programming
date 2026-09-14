# 🟠 cheapest-flights-within-k-stops — Cheapest Flights Within K Stops

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Cheapest Flights Within K Stops on LeetCode.

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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[float('inf')]*n
        dist[src]=0
        for _ in range(k+1):
            temp=dist.copy()
            for u,v,w in flights:
                if dist[u] != float('inf'):
                    temp[v]=min(temp[v],dist[u]+w)
            dist=temp
        return dist[dst] if dist[dst] != float('inf') else -1
```

</details>
