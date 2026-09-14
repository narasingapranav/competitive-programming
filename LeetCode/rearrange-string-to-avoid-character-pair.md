# 🟠 rearrange-string-to-avoid-character-pair — Rearrange String to Avoid Character Pair

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Accepted solution for Rearrange String to Avoid Character Pair on LeetCode.

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
from itertools import permutations
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        f=m=l=""
        for i in s:
            if i==y:
                f+=i
            elif i==x:
                l+=i
            else:
                m+=i
        return f+m+l
```

</details>
