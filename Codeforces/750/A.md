# 🔵 750A — New Year and Hurry

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/750/A) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Determine the maximum number of problems Limak can solve within a 240-minute contest, given that he needs k minutes to travel to a party and the i-th problem takes 5*i minutes to solve.

## 🔍 Key Observation

Limak has 240 - k minutes available for problems; since the problem time increments strictly by 5*i, he should greedily solve problems in order from 1 to n until time runs out.

## ⚙️ Algorithm

**Greedy simulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`implementation` `math` `brute force`

<details>
<summary>💻 View solution</summary>

```python
n,k=map(int,input().split())
remtime=240-k
c=0
for i  in range(1,n+1):
    remtime-=5*i
    if remtime<0:
        break
    c+=1
print(c)
```

</details>
