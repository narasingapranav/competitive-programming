# 🔵 155A — I_love_\%username\%

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/155/A) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Accepted solution for I_love_\%username\% on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`brute force`

<details>
<summary>💻 View solution</summary>

```python
import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
c=0
mi=l[0]
mx=l[0]
for i in range(1,n):
    if l[i]<mi:
        mi=l[i]
        c+=1
    elif l[i]>mx:
        mx=l[i]
        c+=1
print(c)
```

</details>
