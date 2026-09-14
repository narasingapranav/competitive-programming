# 🟠 find-peak-element — Find Peak Element

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-peak-element/) &nbsp;|&nbsp; **Solved:** 2025-12-11

---

## 📝 Summary

Accepted solution for Find Peak Element on LeetCode.

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
    def findPeakElement(self, nums: List[int]) -> int:
        #return(nums.index(max(nums)))
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid+1]<nums[mid]:
                r=mid
            elif nums[mid+1]>nums[mid]:
                l=mid+1
        return l
```

</details>
