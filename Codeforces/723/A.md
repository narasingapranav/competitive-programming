# 🔵 723A — The New Year: Meeting Friends

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/723/A) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Find the minimum total distance three friends on a 1D coordinate line need to travel to meet at the same location.

## 🔍 Key Observation

The optimal meeting point is the median of the three positions, making the total distance traveled equal to the difference between the maximum and minimum positions.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `math` `sortings`

<details>
<summary>💻 View solution</summary>

```python
a, b, c = sorted(map(int, input().split()))
print((b - a) + (c - b))
```

</details>
