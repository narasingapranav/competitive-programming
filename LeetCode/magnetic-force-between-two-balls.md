# 🟠 magnetic-force-between-two-balls — Magnetic Force Between Two Balls

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/magnetic-force-between-two-balls/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Given an array of basket positions and a number of balls m, place all m balls into distinct baskets such that the minimum magnetic force (distance) between any two balls is maximized.

## 🔍 Key Observation

The feasibility of placing m balls with a guaranteed minimum distance d is monotonic, allowing us to binary search for the maximum possible minimum distance.

## ⚙️ Algorithm

**Binary search on answer + Greedy check**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n + n log(max_pos - min_pos))` | `O(n)` |

## 🏷️ Tags

`binary-search` `greedy` `sorting` `array`

<details>
<summary>💻 View solution</summary>

```python
import math
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def solve(dist):
            c=1
            last=position[0]
            for i in position[1:]:
                if i-last>=dist:
                    c+=1
                    last=i
                    if c==m:
                        return True
            return False
        position.sort()
        l=1
        h=position[-1]-position[0]
        while l<=h:
            mid=l+(h-l)//2
            if solve(mid):
                l=mid+1
            else:
                h=mid-1
        return h
```

</details>
