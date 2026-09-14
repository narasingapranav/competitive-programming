# 🟠 n-repeated-element-in-size-2n-array — N-Repeated Element in Size 2N Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) &nbsp;|&nbsp; **Solved:** 2026-01-02

---

## 📝 Summary

Accepted solution for N-Repeated Element in Size 2N Array on LeetCode.

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
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)
        for i in nums:
            if nums.count(i)==n//2:
                return i
```

</details>
