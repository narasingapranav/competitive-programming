# 🟠 partition-array-according-to-given-pivot — Partition Array According to Given Pivot

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/partition-array-according-to-given-pivot/) &nbsp;|&nbsp; **Solved:** 2026-06-08

---

## 📝 Summary

Accepted solution for Partition Array According to Given Pivot on LeetCode.

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
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        if n==1 : return nums
        res=[]
        l,m=0,0
        for i in nums:
            if i<pivot:
                nums[l]=i
                l+=1
            elif i>pivot:
                res.append(i)
            else:
                m+=1
        return nums[:l]+[pivot]*m+res
```

</details>
