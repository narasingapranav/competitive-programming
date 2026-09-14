# 🟠 search-in-rotated-sorted-array-ii — Search in Rotated Sorted Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-09

---

## 📝 Summary

Given a rotated sorted array that may contain duplicate elements, determine if a given target value exists in the array.

## 🔍 Key Observation

When duplicates make nums[left] equal to nums[mid], we cannot determine which half is strictly sorted, so we increment the left boundary by 1; otherwise, standard rotated binary search logic applies by identifying the sorted half.

## ⚙️ Algorithm

**Binary Search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`binary-search` `array` `two-pointers`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
```

</details>
