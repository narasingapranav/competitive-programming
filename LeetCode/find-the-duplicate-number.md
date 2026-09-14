# 🟠 find-the-duplicate-number — Find the Duplicate Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) &nbsp;|&nbsp; **Solved:** 2025-07-08

---

## 📝 Summary

Accepted solution for Find the Duplicate Number on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            if i in s:
                return i
            s.add(i)
```

</details>
