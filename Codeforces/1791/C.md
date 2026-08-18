# 🔵 1791C — Prepend and Append

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1791/C) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Determine the minimum possible length of the initial binary string given a string that was modified by repeatedly prepending and appending opposite bits.

## 🔍 Key Observation

The operations can be reversed by using two pointers from both ends to strip opposite character pairs ('0' and '1') until the outermost characters match or the pointers cross.

## ⚙️ Algorithm

**Two pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`two-pointers` `implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    b=input()
    l=0
    r=n-1
    while l<r and b[l]!=b[r]:
        l+=1
        r-=1
    print(r-l+1 if l<=r else 0)
```

</details>
