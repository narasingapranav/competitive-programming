# 🟠 maximum-subarray — Maximum Subarray

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-subarray/) &nbsp;|&nbsp; **Solved:** 2025-08-15

---

## 📝 Summary

Accepted solution for Maximum Subarray on LeetCode.

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
    def maxSubArray(self, nums: List[int]) -> int:
        mf=nums[0]
        cm=nums[0]
        for i in range(1,len(nums)):
            cm=max(nums[i],cm+nums[i])
            mf=max(mf,cm)
        return mf
```

</details>
