# 🔵 1742A — Sum

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1742/A) &nbsp;|&nbsp; **Solved:** 2026-08-01

---

## 📝 Summary

Accepted solution for Sum on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no OPENAI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`implementation`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
for _ in range(n):
    a,b,c=map(int,input().split())
    if a+b==c or b+c==a or a+c==b:
        print("YES")
    else:
        print("NO")
```

</details>
