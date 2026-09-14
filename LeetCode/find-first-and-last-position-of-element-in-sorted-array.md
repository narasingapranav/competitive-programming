# 🟠 find-first-and-last-position-of-element-in-sorted-array — Find First and Last Position of Element in Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-03-04

---

## 📝 Summary

Accepted solution for Find First and Last Position of Element in Sorted Array on LeetCode.

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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid= (low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        def last():
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid= (low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        return [first(),last()]
```

</details>
