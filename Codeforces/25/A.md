# 🔵 25A — IQ test

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/25/A) &nbsp;|&nbsp; **Solved:** 2026-08-05

---

## 📝 Summary

Given an array of numbers where all elements except one share the same parity (even or odd), find the 1-based index of the single number that differs in parity.

## 🔍 Key Observation

Checking the parity of just the first three elements is sufficient to identify the majority parity, allowing us to scan for the single element with the opposite parity.

## ⚙️ Algorithm

**Linear scan**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`implementation` `brute force`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
l=list(map(int,input().split()))
rem=[i&1 for i in l[:3]]
m=0 if rem.count(1)>=2 else 1
for i in range(len(l)):
    if l[i]&1==m:
        print(i+1)
        break
```

</details>
