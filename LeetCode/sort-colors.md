# 🟠 sort-colors — Sort Colors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sort-colors/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Given an array of objects colored red, white, or blue (represented as integers 0, 1, and 2), sort them in-place so that objects of the same color are adjacent in the order 0, 1, and 2.

## 🔍 Key Observation

Maintaining three pointers (low, mid, and high) allows partitioning the array into three regions in a single pass by moving 0s to the left and 2s to the right.

## ⚙️ Algorithm

**Dutch National Flag Algorithm**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`array` `two-pointers` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        r=len(nums)-1
        m=0
        while m<=r:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m]==2:
                nums[m],nums[r]=nums[r],nums[m]
                r-=1
            else:
                m+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        
```

</details>
