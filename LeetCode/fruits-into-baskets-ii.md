# 🟠 fruits-into-baskets-ii — Fruits Into Baskets II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/fruits-into-baskets-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Determine the number of unplaced fruit types by matching each fruit sequentially to the leftmost unvisited basket that has sufficient capacity.

## 🔍 Key Observation

The small constraints allow a direct greedy simulation that iterates through the baskets for each fruit to find the first valid available basket.

## ⚙️ Algorithm

**Greedy simulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`array` `greedy` `simulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced
```

</details>
