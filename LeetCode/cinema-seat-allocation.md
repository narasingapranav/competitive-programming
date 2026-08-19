# 🟠 cinema-seat-allocation — Cinema Seat Allocation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Find the maximum number of 4-person families that can be seated in a cinema with n rows of 10 seats, given a list of reserved seats.

## 🔍 Key Observation

Rows without any reserved seats can always fit 2 families, so we only need to process rows containing reservations by checking availability in three specific 4-seat blocks (2-5, 4-7, and 6-9).

## ⚙️ Algorithm

**Hash Map / Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(k)` | `O(k)` |

## 🏷️ Tags

`hash-table` `greedy` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for r, c in reservedSeats:
            reserved[r].add(c)
        possibilities = [
            [2, 3, 4, 5],
            [4, 5, 6, 7],
            [6, 7, 8, 9]
        ]
        c = 2 * n
        for r, seats in reserved.items():
            used = [False] * 3
            for k in range(3):
                possible = True
                for seat in possibilities[k]:
                    if seat in seats:
                        possible = False
                        break
                if possible:
                    used[k] = True
            if used[0] and used[2]:
                continue
            elif used[0] or used[1] or used[2]:
                c -= 1
            else:
                c -= 2
        return c
```

</details>
