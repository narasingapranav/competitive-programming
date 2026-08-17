# 🔵 1760A — Medium Number

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1760/A) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Given three distinct integers, find the medium number, which is the value strictly between the minimum and maximum.

## 🔍 Key Observation

In a set of three distinct integers, the medium number is the single element that is equal to neither the minimum nor the maximum.

## ⚙️ Algorithm

**Implementation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) per testcase` | `O(1)` |

## 🏷️ Tags

`implementation` `sortings`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    mx,mi=max(l),min(l)
    for i in l:
        if i!=mx and i!=mi:
            print(i)
            break
```

</details>
