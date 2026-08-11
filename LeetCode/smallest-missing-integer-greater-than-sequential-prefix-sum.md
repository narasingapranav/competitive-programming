# 🟠 smallest-missing-integer-greater-than-sequential-prefix-sum — Smallest Missing Integer Greater Than Sequential Prefix Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Find the sum of the longest sequential prefix starting at index 0, then identify the smallest integer greater than or equal to this sum that is missing from the array.

## 🔍 Key Observation

The sequential prefix ends at the first index where nums[i] != nums[i-1] + 1; starting from the sum of this prefix, we continuously increment by 1 until reaching a value not present in the array.

## ⚙️ Algorithm

**Prefix Scan + HashSet/Linear Search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(1)` |

## 🏷️ Tags

`array` `hash-table` `simulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        su=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                su+=nums[i]
            else:
                break
        while su in nums:
            su+=1
        return su
```

</details>
