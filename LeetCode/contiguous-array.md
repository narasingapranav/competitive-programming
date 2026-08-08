# 🟠 contiguous-array — Contiguous Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/contiguous-array/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Find the maximum length of a contiguous binary subarray with an equal number of 0s and 1s.

## 🔍 Key Observation

Treating 0 as -1 reduces the problem to finding the longest subarray with a sum of 0, which occurs between two identical prefix sums.

## ⚙️ Algorithm

**Prefix sum + Hash table**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`prefix-sum` `hash-table` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        s=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                s-=1
            else:
                s+=1
            if s in d:
                ans=max(i-d[s],ans)
            else:
                d[s]=i
        return ans
```

</details>
