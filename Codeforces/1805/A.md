# 🔵 1805A — We Need the Zero

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1805/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Find an integer x such that XORing every element of an array with x results in a final array whose total XOR sum is zero.

## 🔍 Key Observation

Applying x to all n elements changes the total XOR sum to S ^ x if n is odd, and leaves it as S if n is even (where S is the initial total XOR sum of the array).

## ⚙️ Algorithm

**Bitwise XOR logic**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`bitmasks` `math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=0
    for i in l:
        x^=i
    if n%2==0:
        if x==0:
            print(0)
        else:
            print(-1)
    else:
        print(x)
```

</details>
