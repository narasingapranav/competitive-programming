# 🔵 4C — Registration System

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/4/C) &nbsp;|&nbsp; **Solved:** 2026-08-01

---

## 📝 Summary

Accepted solution for Registration System on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`data structures` `hashing` `implementation`

<details>
<summary>💻 View solution</summary>

```python
from collections import Counter
n=int(input())
s=[input() for _ in range(n)]
c=Counter(s)
initialcount={i: c[i] for i in c}
for i in s:
    if c[i]==initialcount[i]:
        print("OK")
        c[i]-=1
    else:
        print(i+str(initialcount[i]-c[i]))
        c[i]-=1
```

</details>
