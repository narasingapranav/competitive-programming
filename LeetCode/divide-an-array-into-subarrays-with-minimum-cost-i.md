# 🟠 divide-an-array-into-subarrays-with-minimum-cost-i — Divide an Array Into Subarrays With Minimum Cost I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/) &nbsp;|&nbsp; **Solved:** 2026-02-01

---

## 📝 Summary

Accepted solution for Divide an Array Into Subarrays With Minimum Cost I on LeetCode.

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
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        min1, min2 = float('inf'), float('inf')
        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
        
        return first + min1 + min2
```

</details>
