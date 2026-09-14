# 🟠 search-in-rotated-sorted-array — Search in Rotated Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-07-04

---

## 📝 Summary

Accepted solution for Search in Rotated Sorted Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Two pointers**

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
    def search(self, nums: List[int], target: int) -> int:
        ans = -1 
        left = 0 
        right = len(nums) -1 
        while left <= right :
            mid = (left + right)// 2 
            if nums[mid] == target :
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1 
            else:
                if nums[mid] < target <= nums[right] :
                    left = mid + 1 
                else:
                    right = mid - 1 
        return ans
```

</details>
