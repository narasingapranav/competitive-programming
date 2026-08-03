# 🔵 580A — Kefa and First Steps

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/580/A) &nbsp;|&nbsp; **Solved:** 2026-08-01

---

## 📝 Summary

Accepted solution for Kefa and First Steps on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`brute force` `dp` `implementation`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
l=list(map(int,input().split()))
c=1
maxc=1
for i in range(0,n-1):
    if l[i]>l[i+1]:
        c=1
    else:
        c+=1
    maxc=max(maxc,c)
print(maxc)
```

</details>
