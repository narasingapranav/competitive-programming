# 🟠 min-cost-to-connect-all-points — Min Cost to Connect All Points

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Accepted solution for Min Cost to Connect All Points on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        pq=[]
        for i in range(n-1):
            for j in range(i+1,n):
                c=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append((j,c))
                adj[j].append((i,c))
        vis=[False]*n
        res=0
        heapq.heappush(pq,(0,0))
        while pq:
            c,u=heapq.heappop(pq)
            if vis[u]:
                continue
            vis[u]=True
            res+=c
            for b in adj[u]:
                if not vis[b[0]]:
                    heapq.heappush(pq,(b[1],b[0]))
        return res

```

</details>
