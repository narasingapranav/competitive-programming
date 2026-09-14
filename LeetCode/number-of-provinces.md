# 🟠 number-of-provinces — Number of Provinces

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-provinces/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Number of Provinces on LeetCode.

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
    def findCircleNum(self, graph: List[List[int]]) -> int:
        n=len(graph)
        def dfs(graph,vi,v):
            vi[v]=True
            for i in range(n):
                if graph[v][i]==1 and not vi[i]:
                    dfs(graph,vi,i)
        cnt=0
        vi=[False]*n
        for i in range(n):
            if not vi[i]:
                dfs(graph,vi,i)
                cnt+=1
        return cnt
```

</details>
