# 🟠 unique-3-digit-even-numbers — Unique 3-Digit Even Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/) &nbsp;|&nbsp; **Solved:** 2026-09-11

---

## 📝 Summary

Given an array of digits, count how many unique 3-digit even numbers can be formed without leading zeros.

## 🔍 Key Observation

Instead of generating all numbers, we can fix valid choices for the last digit (even) and first digit (1-9) using digit frequency counts, and then count the remaining unique digits available for the middle position.

## ⚙️ Algorithm

**Frequency counting / Brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`counting` `hash table` `brute force`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def totalNumbers(self, a: List[int]) -> int:
        from collections import Counter

        c = Counter(a)
        ans = 0

        for last in [0, 2, 4, 6, 8]:
            if c[last] == 0:
                continue

            c[last] -= 1

            for first in range(1, 10):
                if c[first] == 0:
                    continue

                c[first] -= 1
                ans += sum(1 for x in c if c[x] > 0)
                c[first] += 1

            c[last] += 1

        return ans
```

</details>
