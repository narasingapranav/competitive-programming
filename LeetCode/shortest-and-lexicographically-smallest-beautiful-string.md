# 🟠 shortest-and-lexicographically-smallest-beautiful-string — Shortest and Lexicographically Smallest Beautiful String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/) &nbsp;|&nbsp; **Solved:** 2026-08-26

---

## 📝 Summary

Accepted solution for Shortest and Lexicographically Smallest Beautiful String on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        m = n + 1
        ans = ""
        for i in range(n):
            su = 0
            for j in range(i, n):
                su += int(s[j])
                if su == k:
                    sub = s[i:j+1]
                    if len(sub) < m or (len(sub) == m and sub < ans):
                        m = len(sub)
                        ans = sub
                    break
        return ans
```

</details>
