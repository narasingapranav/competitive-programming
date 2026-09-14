# 🟠 transformed-array — Transformed Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/transformed-array/) &nbsp;|&nbsp; **Solved:** 2026-02-05

---

## 📝 Summary

Accepted solution for Transformed Array on LeetCode.

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
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            target = (i + nums[i]) % n
            res.append(nums[target])
        return res
```

</details>
