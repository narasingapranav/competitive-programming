# 🔵 32B — Borze

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/32/B) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Accepted solution for Borze on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`expression parsing` `implementation`

<details>
<summary>💻 View solution</summary>

```python
l = input()
ans = ''
i = 0
while i < len(l):
    if l[i] == '.':
        ans += '0'
        i += 1
    elif l[i:i+2] == '-.':
        ans += '1'
        i += 2
    elif l[i:i+2] == '--':
        ans += '2'
        i += 2
print(ans)
```

</details>
