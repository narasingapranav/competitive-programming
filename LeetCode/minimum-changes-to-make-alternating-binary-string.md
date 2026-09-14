# 🟠 minimum-changes-to-make-alternating-binary-string — Minimum Changes To Make Alternating Binary String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/) &nbsp;|&nbsp; **Solved:** 2026-03-05

---

## 📝 Summary

Accepted solution for Minimum Changes To Make Alternating Binary String on LeetCode.

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
    def minOperations(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            if int(s[i]) != i%2:
                res+=1
        return min(res,len(s)-res)
```

</details>
