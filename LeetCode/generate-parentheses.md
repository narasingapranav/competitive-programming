# 🟠 generate-parentheses — Generate Parentheses

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/generate-parentheses/) &nbsp;|&nbsp; **Solved:** 2026-03-06

---

## 📝 Summary

Accepted solution for Generate Parentheses on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def utility(self,op,cp,temp,res,n):
        if op+cp== 2*n:
            res.append(temp)
        if op<n:
            self.utility(op+1,cp,temp+'(',res,n)
        if cp<op:
            self.utility(op,cp+1,temp+')',res,n)
        return res
    def generateParenthesis(self, n: int) -> List[str]:
        op=0
        cp=0
        temp=""
        res=[]
        self.utility(op,cp,temp,res,n)
        return res
```

</details>
