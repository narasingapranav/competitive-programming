# 🟠 count-the-number-of-special-characters-i — Count the Number of Special Characters I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-i/) &nbsp;|&nbsp; **Solved:** 2026-05-26

---

## 📝 Summary

Accepted solution for Count the Number of Special Characters I on LeetCode.

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
    def numberOfSpecialChars(self, word: str) -> int:
        a="abcdefghijklmnopqrstuvwxyz"
        s=set(word)
        count=0
        for i in a:
            if i in s and i.upper() in s:
                count+=1
        return count

```

</details>
