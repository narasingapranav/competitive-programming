# 🔵 1791A — Codeforces Checking

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1791/A) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Given a single lowercase Latin character, determine whether it appears in the string "codeforces".

## 🔍 Key Observation

A single character's presence in a small, fixed target string can be checked directly using a simple membership operation.

## ⚙️ Algorithm

**String lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    c=input()
    if c in 'codeforces':
        print('YES')
    else:
        print('NO')
```

</details>
