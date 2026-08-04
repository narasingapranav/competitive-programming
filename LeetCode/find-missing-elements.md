# 🟠 find-missing-elements — Find Missing Elements

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-missing-elements/) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Given an array of integers, find all missing integers within the inclusive range from the minimum to the maximum value of the array.

## 🔍 Key Observation

The bounds of the full sequence are determined by the minimum and maximum elements in the input, so any missing values must lie strictly between these two values.

## ⚙️ Algorithm

**Range iteration**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N * (max - min))` | `O(max - min)` |

## 🏷️ Tags

`array` `search` `iteration`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi,mx=min(nums),max(nums)
        res=[]
        for i in range(mi,mx+1):
            if i not in nums:
                res.append(i)
        return res
```

</details>
