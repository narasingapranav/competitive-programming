# 🔵 1899A — Game with Integers

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1899/A) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Determine if the first player can make a given integer divisible by 3 in at most 10 moves by adding or subtracting 1 on each turn.

## 🔍 Key Observation

If the starting integer is not divisible by 3, the first player can win in a single move by adding or subtracting 1. If it is already divisible by 3, any move by the first player makes it non-divisible, allowing the second player to restore it back to a multiple of 3.

## ⚙️ Algorithm

**Modular arithmetic**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`games` `math` `number theory`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
for _ in range(n):
    i=int(input())
    if i%3==0:
        print("Second")
    else:
        print("First")

# 0 1 2 3
# S F F S
```

</details>
