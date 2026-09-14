# 🟠 product-of-array-except-self — Product of Array Except Self

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/) &nbsp;|&nbsp; **Solved:** 2026-07-01

---

## 📝 Summary

Accepted solution for Product of Array Except Self on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=[0]*len(nums)
        sf=[0]*len(nums)
        res=[0]*len(nums)
        pf[0]=sf[len(nums)-1]=1
        for i in range(1,len(nums)):
            pf[i]=pf[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            sf[i]=sf[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=pf[i]*sf[i]
        return res
```

</details>
