# 🟠 third-maximum-number — Third Maximum Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/third-maximum-number/) &nbsp;|&nbsp; **Solved:** 2025-12-24

---

## 📝 Summary

Accepted solution for Third Maximum Number on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        if len(s)<3:
            return max(s)
        s.remove(max(s))
        s.remove(max(s))
        return max(s)
```

</details>
