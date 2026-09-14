# 🟠 score-of-a-string — Score of a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/score-of-a-string/) &nbsp;|&nbsp; **Solved:** 2026-05-27

---

## 📝 Summary

Accepted solution for Score of a String on LeetCode.

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
    def scoreOfString(self, s: str) -> int:
        tot=0
        for i in range(len(s)-1):
            tot+=abs(ord(s[i])-ord(s[i+1]))
        return tot
```

</details>
