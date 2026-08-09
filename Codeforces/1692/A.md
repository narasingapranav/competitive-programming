# 🔵 1692A — Marathon

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1692/A) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Count how many of the three other participants ran a distance strictly greater than Timur's distance.

## 🔍 Key Observation

Timur's distance is given first, so we only need to iterate over the remaining three values and count how many exceed his distance.

## ⚙️ Algorithm

**Linear scan**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) per test case` | `O(1)` |

## 🏷️ Tags

`implementation` `counting`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    tim=l[0]
    c=0
    for i in range(1,len(l)):
        if l[i]>tim:
            c+=1
    print(c)
```

</details>
