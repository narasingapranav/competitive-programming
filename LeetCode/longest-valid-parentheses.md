# 🟠 longest-valid-parentheses — Longest Valid Parentheses

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-valid-parentheses/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Accepted solution for Longest Valid Parentheses on LeetCode.

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
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        st=[-1]
        cnt=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if len(st)==0:
                    st.append(i)
                else:
                    cnt=max(cnt,i-st[-1])
        return cnt
```

</details>
