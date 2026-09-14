# 🟠 find-all-numbers-disappeared-in-an-array-ii — Find All Numbers Disappeared in an Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Accepted solution for Find All Numbers Disappeared in an Array II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        res=[]
        prev=lower-1
        for i in nums:
            if i<lower or i>upper:
                continue
            if i>prev+1:
                res.append((prev+1,i-1))
            prev=i
        if prev<upper:
            res.append((prev+1,upper))
        return res
```

</details>
