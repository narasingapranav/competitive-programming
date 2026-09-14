# 🟠 search-in-rotated-sorted-array — Search in Rotated Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-05-22

---

## 📝 Summary

Accepted solution for Search in Rotated Sorted Array on LeetCode.

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
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        low, high = 0, n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[high]:
                if nums[mid] >= target and nums[low] <= target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] <= target and nums[high] >= target:
                    low = mid+1
                else:
                    high = mid-1
        return -1
```

</details>
