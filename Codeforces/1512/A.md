# 🔵 1512A — Spy Detected!

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1512/A) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Find the 1-based index of the single element in an array that differs from all other elements, which are all identical.

## 🔍 Key Observation

The unique element is the only value in the array with a frequency equal to 1.

## ⚙️ Algorithm

**Linear search with frequency counting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`implementation` `brute force` `arrays`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a.count(a[i]) == 1:
            print(i + 1)
            break
```

</details>
