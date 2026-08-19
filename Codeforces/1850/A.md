# 🔵 1850A — To My Critics

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1850/A) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Given three single-digit integers, determine if any pair of them sums up to 10 or greater.

## 🔍 Key Observation

Since there are only three numbers, we can directly check the sums of all three possible pairs against the threshold of 10.

## ⚙️ Algorithm

**Conditional check**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a+b>=10 or b+c>=10 or a+c>=10:
        print("YES")
    else:
        print("NO")
```

</details>
