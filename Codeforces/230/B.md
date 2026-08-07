# 🔵 230B — T-primes

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/230/B) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Determine whether each given integer has exactly three distinct positive divisors (a T-prime).

## 🔍 Key Observation

A number has exactly three positive divisors if and only if it is the square of a prime number.

## ⚙️ Algorithm

**Trial division / Square root divisor counting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * sqrt(x))` | `O(n)` |

## 🏷️ Tags

`math` `number-theory` `implementation`

<details>
<summary>💻 View solution</summary>

```python
def countdiv(n):
    c=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            c+=1
            if i!=n//i:
                c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if countdiv(i)==3:
        print("YES")
    else:
        print("NO")
'''
1
999966000289

'''
```

</details>
