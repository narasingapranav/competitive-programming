# 🔵 1374B — Multiply by 2, divide by 6

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1374/B) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Determine the minimum number of operations to reduce $n$ to $1$ using two operations: multiply by $2$ or divide by $6$, or determine if it is impossible.

## 🔍 Key Observation

Dividing by $6$ reduces the prime factor counts of both $2$ and $3$ by one, while multiplying by $2$ increases the count of $2$ by one; thus, a solution exists if and only if $n$ has no prime factors other than $2$ and $3$, and the exponent of $2$ does not exceed the exponent of $3$.

## ⚙️ Algorithm

**Prime factorization / Math**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(1)` |

## 🏷️ Tags

`math` `number theory`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    a=b=0
    while n%2==0:
        n//=2
        a+=1
    while n%3==0:
        n//=3
        b+=1
    if n!=1 and a>b:
        print(-1)
    else:
        print(2*b-a)
```

</details>
