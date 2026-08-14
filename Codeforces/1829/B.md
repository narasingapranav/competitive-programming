# 🔵 1829B — Blank Space

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1829/B) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Find the maximum length of a contiguous subarray consisting entirely of zeros in a given binary array.

## 🔍 Key Observation

Traverse the array while tracking the current count of consecutive zeros, updating the global maximum when encountering a zero and resetting the count when encountering a one.

## ⚙️ Algorithm

**Linear scan**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`implementation` `array`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    c=0
    for i in range(n):
        if a[i]==0:
            c+=1
            m=max(m,c)
        else:
            c=0
    print(m)
```

</details>
