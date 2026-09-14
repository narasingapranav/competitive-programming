# 🟠 number-of-ways-to-assign-edge-weights-i — Number of Ways to Assign Edge Weights I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/) &nbsp;|&nbsp; **Solved:** 2026-06-11

---

## 📝 Summary

Accepted solution for Number of Ways to Assign Edge Weights I on LeetCode.

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
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 1_000_000_007
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, prev: int) -> int:
            d = 0
            for c in graph[node]:
                if c != prev:
                    d = max(d, dfs(c, node) + 1)
            return d

        return pow(2, dfs(1, 0) - 1, mod)
```

</details>
