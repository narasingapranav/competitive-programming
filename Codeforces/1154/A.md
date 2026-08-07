# 🔵 1154A — Restoring Three Numbers

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1154/A) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Given four integers representing the three pairwise sums and the total sum of three hidden positive integers in arbitrary order, recover the three original integers.

## 🔍 Key Observation

The largest of the four given numbers must be the total sum (a + b + c), which leaves the other three numbers as the pairwise sums (a + b, a + c, and b + c).

## ⚙️ Algorithm

**System of linear equations**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`math` `implementation`

<details>
<summary>💻 View solution</summary>

```python
l=list(map(int,input().split()))
t=max(l)
l.pop(l.index(t))
x,y,z=l
a=(x+y-z)//2
b=(x+z-y)//2
c=(y+z-x)//2
print(a,b,c)
```

</details>
