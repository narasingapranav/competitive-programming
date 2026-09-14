# 🟠 lexicographically-smallest-generated-string — Lexicographically Smallest Generated String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-generated-string/) &nbsp;|&nbsp; **Solved:** 2026-03-31

---

## 📝 Summary

Accepted solution for Lexicographically Smallest Generated String on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def generateString(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        ans = ['?'] * (n + m - 1)  # ? indicates a pending position
        
        # Process 'T'
        for i, b in enumerate(s):
            if b != 'T':
                continue
            # The substring must match t
            for j, c in enumerate(t):
                v = ans[i + j]
                if v != '?' and v != c:
                    return ""
                ans[i + j] = c
        
        old_ans = ans
        ans = ['a' if c == '?' else c for c in ans]  # Initial default is 'a'
        
        # Process 'F'
        for i, b in enumerate(s):
            if b != 'F':
                continue
            # Substring must not equal t
            if ''.join(ans[i: i + m]) != t:
                continue
            # Locate the last pending position to modify
            for j in range(i + m - 1, i - 1, -1):
                if old_ans[j] == '?':  # Change 'a' to 'b'
                    ans[j] = 'b'
                    break
            else:
                return ""
        return ''.join(ans)
```

</details>
