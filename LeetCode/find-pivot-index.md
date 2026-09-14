# 🟠 find-pivot-index — Find Pivot Index

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-pivot-index/) &nbsp;|&nbsp; **Solved:** 2025-09-25

---

## 📝 Summary

Accepted solution for Find Pivot Index on LeetCode.

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
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:])==0:
            return 0
        for i in range(1,len(nums)):
           ls=sum(nums[:i])
           rs=sum(nums[(i+1):])
           if ls==rs:
                return i
        return -1
```

</details>
