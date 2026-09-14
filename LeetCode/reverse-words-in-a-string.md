# 🟠 reverse-words-in-a-string — Reverse Words in a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/) &nbsp;|&nbsp; **Solved:** 2026-09-07

---

## 📝 Summary

Given a string containing words separated by spaces, return a string with the words in reverse order separated by a single space, removing any leading or trailing whitespace.

## 🔍 Key Observation

Splitting the string implicitly strips extra whitespace and breaks it into an array of words, which can then be reversed and rejoined.

## ⚙️ Algorithm

**String Splitting and Reversal**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`string` `parsing`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.strip().split()
        return " ".join(l[::-1])
```

</details>
