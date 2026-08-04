# 🔵 230A — Dragons

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/230/A) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Determine whether Kirito can defeat all dragons in a game given his initial strength, where each dragon requires a certain strength to defeat and grants bonus strength upon defeat.

## 🔍 Key Observation

Fighting the dragons in ascending order of their strength requirements maximizes the chance of defeating all of them, as weaker dragons provide strength boosts needed for stronger ones.

## ⚙️ Algorithm

**Greedy + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`greedy` `sorting`

<details>
<summary>💻 View solution</summary>

```python
s,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
l.sort(key=lambda x:x[0])
for i in l:
    s-=i[0]
    if s<=0:
        print("NO")
        break
    s+=i[0]+i[1]
else:
    print("YES")
```

</details>
