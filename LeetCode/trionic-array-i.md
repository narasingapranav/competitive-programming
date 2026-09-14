# 🟠 trionic-array-i — Trionic Array I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/trionic-array-i/) &nbsp;|&nbsp; **Solved:** 2025-08-16

---

## 📝 Summary

Accepted solution for Trionic Array I on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        def is_strictly_increasing(arr: list[int], start: int, end: int) -> bool:
            for i in range(start + 1, end + 1):
                if arr[i] <= arr[i - 1]:
                    return False
            return True
        def is_strictly_decreasing(arr: list[int], start: int, end: int) -> bool:
            for i in range(start + 1, end + 1):
                if arr[i] >= arr[i - 1]:
                    return False
            return True
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                if (is_strictly_increasing(nums, 0, p) and
                        is_strictly_decreasing(nums, p, q) and
                        is_strictly_increasing(nums, q, n - 1)):
                    return True
        return False
```

</details>
