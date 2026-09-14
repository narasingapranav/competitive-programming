# 🟠 basic-calculator — Basic Calculator

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/basic-calculator/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Basic Calculator on LeetCode.

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
    def calculate(self, s: str) -> int:
        ans=0
        n=0
        sign=1
        st=[sign]
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="(":
                st.append(sign)
            elif i==")":
                st.pop()
            elif i=='+' or i=='-':
                ans+=sign*n
                sign=(1 if i=='+' else -1)*st[-1]
                n=0
        return ans+sign*n
```

</details>
