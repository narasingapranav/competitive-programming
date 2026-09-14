# 🟠 minimum-adjacent-swaps-to-partition-array — Minimum Adjacent Swaps to Partition Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Accepted solution for Minimum Adjacent Swaps to Partition Array on LeetCode.

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
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        mod, c1, c2, res = 10 ** 9 + 7, 0, 0, 0
        for x in nums:
            if x < a:
                res = (res + c1 + c2) % mod
            elif x <= b:
                res = (res + c2) % mod
                c1 += 1
            else:
                c2 += 1
        return res
```

</details>
