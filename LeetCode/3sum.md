# 🟠 3sum — 3Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/3sum/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Find all unique triplets in an integer array that sum up to zero.

## 🔍 Key Observation

Sorting the array allows skipping duplicate values to ensure unique triplets, while a hash map mapping each number to its last index enables checking for the third element in O(1) time.

## ⚙️ Algorithm

**Sorting + Hash Map**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`array` `hash-table` `sorting` `two-pointers`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        if nums[0]>0 :
            return res
        n=len(nums)
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(n-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-1):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                k=-(nums[i]+nums[j])
                if k in d and d[k]>j:
                    res.append([nums[i],nums[j],k])
        return res
```

</details>
