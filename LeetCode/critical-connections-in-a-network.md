# 🟠 critical-connections-in-a-network — Critical Connections in a Network

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Accepted solution for Critical Connections in a Network on LeetCode.

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
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        time=1
        def dfs(adj,src,par,vis):
            nonlocal time
            vis[src]=True
            disc[src]=low[src]=time
            time+=1
            for v in adj[src]:
                if v==par:
                    continue
                if vis[v]:
                    low[src]=min(low[src],low[v])
                else:
                    dfs(adj,v,src,vis)
                    low[src]=min(low[src],low[v])
                    if low[v]>disc[src]:
                        res.append((src,v))


        res=[]
        disc=[0]*n
        low=[0]*n
        vis=[False]*n
        adj=defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        dfs(adj,0,-1,vis)
        return res
```

</details>
