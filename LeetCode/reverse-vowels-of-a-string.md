# 🟠 reverse-vowels-of-a-string — Reverse Vowels of a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/) &nbsp;|&nbsp; **Solved:** 2026-03-12

---

## 📝 Summary

Accepted solution for Reverse Vowels of a String on LeetCode.

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
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] not in vowels:
                l += 1
                continue
            if s[r] not in vowels:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
```

</details>
