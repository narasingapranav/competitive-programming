# 🟠 push-dominoes — Push Dominoes

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/push-dominoes/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Push Dominoes on LeetCode.

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
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        f=[0]*n
        fo=0
        for i in range(n):
            if dominoes[i]=='L':
                fo=0
            elif dominoes[i]=='R':
                fo=n
            else:
                fo=max(fo-1,0)
            f[i]+=fo
        fo=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=='R':
                fo=0
            elif dominoes[i]=='L':
                fo=n
            else:
                fo=max(fo-1,0)
            f[i]-=fo
        res=[]
        for i in f:
            if i>0:
                res.append('R')
            elif i<0:
                res.append('L')
            else:
                res.append('.')
        return "".join(res)
```

</details>
