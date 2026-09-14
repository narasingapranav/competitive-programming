# 🟠 sorted-gcd-pair-queries — Sorted GCD Pair Queries

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sorted-gcd-pair-queries/) &nbsp;|&nbsp; **Solved:** 2026-07-20

---

## 📝 Summary

Accepted solution for Sorted GCD Pair Queries on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Binary search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`binary-search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def gcdValues(self, A: list[int], queries: list[int]) -> list[int]:
        mx = max(A)
        freq = [0] * (mx + 1)
        for a in A: 
            freq[a] += 1
        GCD = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            GCD[i] = sm * (sm - 1) // 2 - sum(GCD[i::i])
        GCD = list(accumulate(GCD))
        return [bisect.bisect_right(GCD, q) for q in queries]
```

</details>
