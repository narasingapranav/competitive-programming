# 🟠 two-furthest-houses-with-different-colors — Two Furthest Houses With Different Colors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/two-furthest-houses-with-different-colors/) &nbsp;|&nbsp; **Solved:** 2026-04-20

---

## 📝 Summary

Accepted solution for Two Furthest Houses With Different Colors on LeetCode.

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
    def maxDistance(self, A: List[int]) -> int:
        n = len(A)
        left, right = 0, n - 1

        for i in range(n):
            if A[i] ^ A[-1]:
                left = i
                break

        for i in range(n - 1, -1, -1):
            if A[i] ^ A[0]:
                right = i
                break

        return max(n - 1 - left, right)
```

</details>
