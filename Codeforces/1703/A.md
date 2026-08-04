# 🔵 1703A — YES or YES?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1703/A) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Determine whether a given 3-character string is equal to 'YES', ignoring letter casing.

## 🔍 Key Observation

Converting the input string to a uniform case (e.g., lowercase) allows for a simple direct comparison with 'yes'.

## ⚙️ Algorithm

**String manipulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`strings` `implementation`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
for _ in range(n):
    s=input().lower()
    if s=="yes":
        print("YES")
    else:
        print("NO")
```

</details>
