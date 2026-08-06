# 🔵 1669A — Division?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1669/A) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Given a player's rating, determine which division (Division 1, 2, 3, or 4) they belong to based on predefined rating ranges.

## 🔍 Key Observation

The division boundaries are fixed and non-overlapping, so simple conditional statements (if-elif-else) can directly categorize each rating.

## ⚙️ Algorithm

**Implementation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `conditionals`

<details>
<summary>💻 View solution</summary>

```python
n=int(input())
for _ in range(n):
    rating=int(input())
    if 1900<=rating:
        print("Division 1")
    elif 1600<=rating<=1899:
        print("Division 2")
    elif 1400<=rating<=1599:
        print("Division 3")
    else:
        print("Division 4")
```

</details>
