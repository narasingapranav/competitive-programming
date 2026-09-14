# 🟠 find-minimum-in-rotated-sorted-array-ii — Find Minimum in Rotated Sorted Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-05-16

---

## 📝 Summary

Accepted solution for Find Minimum in Rotated Sorted Array II on LeetCode.

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
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]<nums[h]:

                h=mid
            elif nums[mid]>nums[h]:
                l=mid+1          
            else:
                h-=1
        return nums[l]

'''

2,2,2,0,1

  2,2,0,1
   
    2,0,1

     0,1

     0




'''
```

</details>
