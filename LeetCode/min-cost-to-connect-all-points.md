# 🟠 min-cost-to-connect-all-points — Min Cost to Connect All Points

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Min Cost to Connect All Points on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`graph` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create a graph
        g=defaultdict(list)
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                g[i].append((j,dist))
                g[j].append((i,dist))
        # total cost=0 , take a visited set
        tc=0
        vis=set()
        # create a min heap
        h=[(0,0)]
        n=len(points)
        while len(vis)<n:
            # pop the node and check if visited if not add distance and pudh neighbour heap
            dis,nod=heapq.heappop(h)
            if nod in vis:
                continue
            vis.add(nod)
            tc+=dis
            for nei,wei in g[nod]:
                if nei not in vis:
                    heapq.heappush(h,(wei,nei))
        return tc
```

</details>
