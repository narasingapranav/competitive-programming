# 🟠 minimize-hamming-distance-after-swap-operations — Minimize Hamming Distance After Swap Operations

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/) &nbsp;|&nbsp; **Solved:** 2026-04-21

---

## 📝 Summary

Accepted solution for Minimize Hamming Distance After Swap Operations on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        for u, v in allowedSwaps:
            union(u, v)

        from collections import defaultdict, Counter

        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        answer = 0

        for indices in groups.values():
            freq = Counter()

            for idx in indices:
                freq[source[idx]] += 1

            for idx in indices:
                if freq[target[idx]] > 0:
                    freq[target[idx]] -= 1
                else:
                    answer += 1

        return answer  
```

</details>
