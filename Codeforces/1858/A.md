# 🔵 1858A — Buttons

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1858/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Determine whether the first or second player wins a button-pressing game where players have exclusive buttons and a set of shared buttons.

## 🔍 Key Observation

Both players optimally exhaust all shared buttons first; an odd number of shared buttons effectively gives the first player one extra move advantage, changing the required win condition from a > b to a >= b.

## ⚙️ Algorithm

**Game Theory / Math**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`games` `greedy` `math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if c%2==0:
        if a>b:
            print("First")
        else:
            print("Second")
    else:
        if a>=b:
            print("First")
        else:
            print("Second")
```

</details>
