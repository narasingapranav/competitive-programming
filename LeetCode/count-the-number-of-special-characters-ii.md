# 🟠 count-the-number-of-special-characters-ii — Count the Number of Special Characters II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-ii/) &nbsp;|&nbsp; **Solved:** 2026-05-27

---

## 📝 Summary

Accepted solution for Count the Number of Special Characters II on LeetCode.

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
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in word and i.upper() in word and word.rindex(i) < word.index(i.upper()):
                c+=1
        return c
```

</details>
