# 🟠 minimize-maximum-pair-sum-in-array — Minimize Maximum Pair Sum in Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) &nbsp;|&nbsp; **Solved:** 2026-01-24

---

## 📝 Summary

Accepted solution for Minimize Maximum Pair Sum in Array on LeetCode.

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
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        l = 0
        r = len(nums)-1

        while l<r:
            ans = max(ans, nums[l]+nums[r])
            l+=1
            r-=1
        return ans
```

</details>
