# 🟠 largest-number — Largest Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/largest-number/) &nbsp;|&nbsp; **Solved:** 2026-05-27

---

## 📝 Summary

Accepted solution for Largest Number on LeetCode.

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
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(i) for i in nums]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]+nums[i]>nums[i]+nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        ans="".join(nums)
        return '0' if  ans[0]=='0' else ans
```

</details>
