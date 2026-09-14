# 🟠 number-of-ways-to-assign-edge-weights-ii — Number of Ways to Assign Edge Weights II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/) &nbsp;|&nbsp; **Solved:** 2026-06-12

---

## 📝 Summary

Accepted solution for Number of Ways to Assign Edge Weights II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^7) (estimated -- 7 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
pow2 = [0] * 100_001
pow2[1] = 1
for i in range(2, 100_001):
    pow2[i] = (pow2[i - 1] * 2) % 1_000_000_007


class Solution:
    def assignEdgeWeights(self, edges, queries) -> List[int]:
        g = defaultdict(list)
        for u, v in edges:
            g[min(u, v)].append(max(u, v))

        q = defaultdict(list)
        for i, (u, v) in enumerate(queries):
            q[u].append((v, i))
            q[v].append((u, i))

        n = len(edges) + 2
        uf = list(range(n))
        depth = [0] * n
        lca = [0] * len(queries)

        def find(x: int) -> int:
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        def tarjan(u: int):
            for v in g[u]:
                depth[v] = depth[u] + 1
                tarjan(v)
                uf[v] = u
            for v, i in q[u]:
                if depth[v] != 0:
                    lca[i] = find(v)

        depth[1] = 0
        tarjan(1)

        return [
            pow2[depth[u] + depth[v] - 2 * depth[lca[i]]]
            for i, (u, v) in enumerate(queries)
        ]
```

</details>
