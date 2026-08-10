# 🟠 longest-consecutive-sequence — Longest Consecutive Sequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Find the length of the longest sequence of consecutive elements in an unsorted array of integers.

## 🔍 Key Observation

Sorting the array brings consecutive numbers next to each other, allowing a single linear scan to track and measure sequence lengths while skipping duplicate values.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`array` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        nums.sort()
        m=c=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                m=max(m,c)
            elif nums[i+1]==nums[i]+1:
                c+=1
            else:
                m=max(m,c)
                c=1
        m=max(m,c)     
        return m
```

</details>
