# 🔵 427A — Police Recruits

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/427/A) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Given a sequence of events representing hired police officers and crimes, count how many crimes go untreated assuming each officer can solve at most one crime.

## 🔍 Key Observation

Track the current number of available police officers: if a crime occurs with no officers available, increment the untreated crime count; otherwise, assign an officer to handle it.

## ⚙️ Algorithm

**Greedy simulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`implementation` `greedy` `simulation`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
l=list(map(int,input().split()))
c=0
h=0
for i in range(n):
    if l[i]<0 and h==0:
        c+=1
    if h>0 and l[i]<0:
        h-=1
    if l[i]>0:
        h+=l[i]
print(c)
```

</details>
