# 🟠 maximize-active-section-with-trade-i — Maximize Active Section with Trade I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-i/) &nbsp;|&nbsp; **Solved:** 2026-07-21

---

## 📝 Summary

Accepted solution for Maximize Active Section with Trade I on LeetCode.

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
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        s='1'+s+'1'
        groups = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            groups.append((s[i], j - i))
            i = j
        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                left = groups[i - 1]
                right = groups[i + 1]
                if left[0] == '0' and right[0] == '0':
                    gain = left[1] + right[1]
        mx = 0
        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                if groups[i-1][0] == '0' and groups[i+1][0] == '0':
                    mx = max(mx, groups[i-1][1] + groups[i+1][1])
        return ones+mx
```

</details>
