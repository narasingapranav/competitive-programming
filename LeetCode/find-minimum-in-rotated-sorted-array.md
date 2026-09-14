# 🟠 find-minimum-in-rotated-sorted-array — Find Minimum in Rotated Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) &nbsp;|&nbsp; **Solved:** 2025-12-11

---

## 📝 Summary

Accepted solution for Find Minimum in Rotated Sorted Array on LeetCode.

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
    def findMin(self, nums: List[int]) -> int:
        #return min(nums)
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=nums[l]:
                if nums[mid]>nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[mid]<nums[r]:
                r=mid
        return nums[l]
```

</details>
