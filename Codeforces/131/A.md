# 🔵 131A — cAPS lOCK

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/131/A) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Determine if a string was typed with Caps Lock accidentally enabled (either all uppercase or all uppercase except the first letter) and swap its character casing if so.

## 🔍 Key Observation

The casing should be inverted if and only if every character after the first one is uppercase (or if the string contains only one character).

## ⚙️ Algorithm

**String inspection and case swapping**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
s = input()
if len(s)==1 or s.isupper() or (s[0].islower() and s[1:].isupper()):
    print(s.swapcase())
else:
    print(s)
```

</details>
