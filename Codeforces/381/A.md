# 🔵 381A — Sereja and Dima

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/381/A) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Two players take turns choosing the larger card from either the left or right end of a row of cards. Determine the total sum of cards collected by Sereja and Dima by the end of the game.

## 🔍 Key Observation

In each step, the current player must greedily pick the larger card between the two available cards at the ends of the remaining row.

## ⚙️ Algorithm

**Two pointers / Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`greedy` `two pointers` `implementation`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
l=list(map(int,input().split()))
s=0
d=0
t=1
while len(l)>0:
    if len(l)==1 and t==1:
        s+=l[0]
        break
    if len(l)==1 and t==0:
        d+=l[0]
        break
    s+=max(l[0],l[-1])
    if l[0]>l[-1]:
        l.pop(0)
    else:
        l.pop()
    t=0
    d+=max(l[0],l[-1])
    if l[0]>l[-1]:
        l.pop(0)
    else:
        l.pop()
    t=1
print(s,d)

'''
s-7 5 3 1
d-6 4 2
'''
```

</details>
