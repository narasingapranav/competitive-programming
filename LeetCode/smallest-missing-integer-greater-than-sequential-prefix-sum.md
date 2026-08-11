# 🟠 smallest-missing-integer-greater-than-sequential-prefix-sum — Smallest Missing Integer Greater Than Sequential Prefix Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Calculate the sum of the longest sequential prefix in the array, then find the smallest integer greater than or equal to this sum that is absent from the array.

## 🔍 Key Observation

The sequential prefix ends at the first index where an element is not equal to its predecessor plus one; after calculating its sum, we can use a hash set to efficiently increment to the smallest missing integer.

## ⚙️ Algorithm

**Hash set + Linear scan**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`array` `hash-table` `prefix-sum`

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
        s=set(nums)
        while su in s:
            su+=1
        return su
```

</details>
