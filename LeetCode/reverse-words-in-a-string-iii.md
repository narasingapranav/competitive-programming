# 🟠 reverse-words-in-a-string-iii — Reverse Words in a String III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Accepted solution for Reverse Words in a String III on LeetCode.

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
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        ans=[]
        for i in s:
            ans.append(i[::-1])
        return " ".join(ans)
```

</details>
