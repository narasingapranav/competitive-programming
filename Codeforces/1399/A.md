# 🔵 1399A — Remove Smallest

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1399/A) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Determine if an array of numbers can be reduced to a single element by repeatedly removing the smaller of any two elements with an absolute difference of at most 1.

## 🔍 Key Observation

Sorting the array allows us to check adjacent elements; the array can be reduced to one element if and only if no two adjacent elements in the sorted order differ by more than 1.

## ⚙️ Algorithm

**Sorting + linear scan**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`greedy` `sorting`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(1,n):
        if abs(a[i]-a[i-1])>1:
            print('NO')
            break
    else:
        print("YES")
```

</details>
