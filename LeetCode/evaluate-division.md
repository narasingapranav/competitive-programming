# 🟠 evaluate-division — Evaluate Division

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/evaluate-division/) &nbsp;|&nbsp; **Solved:** 2026-03-02

---

## 📝 Summary

Accepted solution for Evaluate Division on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`graph` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        a=[]
        for (u,v),val in zip(equations,values):
            graph[u].append([v,val])
            graph[v].append([u,1/val])
        n=len(queries)
        def dfs(src,dest,visited,prod):
            if src==dest:
                return prod
            visited.add(src)
            for nei,wei in graph[src]:
                if nei not in visited:
                    ans=dfs(nei,dest,visited,prod*wei)
                    if ans !=-1:
                        return ans
            return -1.0
                     
        res=[]
        for src,dest in queries:
            if src not in graph or dest not in graph:
                res.append(-1.0)
                continue
            else:
                visited=set()
                res.append(dfs(src,dest,visited,1.0))
                continue
        return res
```

</details>
