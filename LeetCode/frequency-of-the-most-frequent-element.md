# 🟠 frequency-of-the-most-frequent-element — Frequency of the Most Frequent Element

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Given an integer array and a maximum of k total increments, return the maximum possible frequency of any element after performing the operations.

## 🔍 Key Observation

Sorting the array allows us to use a sliding window where the cost to make all elements in window [l, r] equal to nums[r] is nums[r] * (r - l + 1) - sum(nums[l..r]). We can maintain the maximum valid window size dynamically.

## ⚙️ Algorithm

**Sorting + Sliding Window**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`sorting` `sliding-window` `two-pointers` `greedy`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        x=k
        nums.sort()
        for r in range(len(nums)):
            x+=nums[r]
            if x<nums[r]*(r-l+1):
                x-=nums[l]
                l+=1
        return len(nums)-l
```

</details>
