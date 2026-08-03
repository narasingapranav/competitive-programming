# 🔵 318A — Even Odds

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/318/A) &nbsp;|&nbsp; **Solved:** 2026-07-30

---

## 📝 Summary

Find the k-th number in a sequence of integers from 1 to n where all odd numbers appear first in ascending order, followed by all even numbers in ascending order.

## 🔍 Key Observation

The total number of odd numbers in the sequence is (n + 1) // 2. If k is less than or equal to this count, the result is the k-th odd number; otherwise, it is the (k - count)-th even number.

## ⚙️ Algorithm

**Math**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`math` `implementation`

<details>
<summary>💻 View solution</summary>

```python
n, k = map(int, input().split())
odd = (n + 1) // 2
if k <= odd:
    print(2 * k - 1)
else:
    print(2 * (k - odd))
```

</details>
