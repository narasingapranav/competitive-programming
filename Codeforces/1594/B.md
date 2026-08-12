# 🔵 1594B — Special Numbers

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1594/B) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Find the k-th smallest integer that can be expressed as a sum of distinct non-negative powers of n, modulo 10^9+7.

## 🔍 Key Observation

The problem is equivalent to interpreting the binary representation of k as a number in base n.

## ⚙️ Algorithm

**Bitwise processing / Base representation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log k)` | `O(1)` |

## 🏷️ Tags

`bitmasks` `math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
MOD=10**9+7
for _ in range(t):
    n,k=map(int,input().split())
    ans=0
    pow=1
    while k>0:
        if k&1:
            ans=(ans+pow)%MOD
        pow=(pow*n)%MOD
        k>>=1
    print(ans)
```

</details>
