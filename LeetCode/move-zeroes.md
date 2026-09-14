# 🟠 move-zeroes — Move Zeroes

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/move-zeroes/) &nbsp;|&nbsp; **Solved:** 2026-06-01

---

## 📝 Summary

Accepted solution for Move Zeroes on LeetCode.

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
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[l]=nums[i]
                l+=1
        while l<len(nums):
            nums[l]=0
            l+=1
                
        """
        Do not return anything, modify nums in-place instead.
        """
        
```

</details>
