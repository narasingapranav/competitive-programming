# 🟠 maximum-distance-between-a-pair-of-values — Maximum Distance Between a Pair of Values

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/) &nbsp;|&nbsp; **Solved:** 2026-04-19

---

## 📝 Summary

Accepted solution for Maximum Distance Between a Pair of Values on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxDistance(self, A: List[int], B: List[int]) -> int:
        i, j = 0, 1

        while i < len(A) and j < len(B):
            i += A[i] > B[j]
            j += 1

        return j - i - 1
```

</details>
