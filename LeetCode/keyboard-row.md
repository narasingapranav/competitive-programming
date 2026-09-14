# 🟠 keyboard-row — Keyboard Row

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/keyboard-row/) &nbsp;|&nbsp; **Solved:** 2026-05-25

---

## 📝 Summary

Accepted solution for Keyboard Row on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        m={}
        for c in "qwertyuiop":
            m[c]=1
        for c in "asdfghjkl":
            m[c]=2
        for c in "zxcvbnm":
            m[c]=3
        ans=[]
        for w in words:
            l=w.lower()
            r=m[l[0]]
            if all(m[c]==r for c in l):
                ans.append(w)
        return ans
```

</details>
