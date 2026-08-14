# 🟠 subarrays-distinct-element-sum-of-squares-i — Subarrays Distinct Element Sum of Squares I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Calculate the sum of the squared counts of distinct elements across all possible contiguous subarrays of an integer array.

## 🔍 Key Observation

For small constraints, we can iterate over all subarray starting indices and incrementally build the set of unique elements as we extend the endpoint, squaring and adding the set size at each step.

## ⚙️ Algorithm

**Brute-force / Hash Set**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`array` `hash table` `brute force`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sq=0
        for i in range(len(nums)):
            s=set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                l=len(s)
                sq+=l**2
        return sq
```

</details>
