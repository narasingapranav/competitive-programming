# 🟠 remove-outermost-parentheses — Remove Outermost Parentheses

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-outermost-parentheses/) &nbsp;|&nbsp; **Solved:** 2026-03-09

---

## 📝 Summary

Accepted solution for Remove Outermost Parentheses on LeetCode.

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
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance = 0
        start = 0
        for i, ch in enumerate(s):
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res.append(s[start + 1:i])
                start = i + 1
        return ''.join(res)
```

</details>
