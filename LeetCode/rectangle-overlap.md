# 🟠 rectangle-overlap — Rectangle Overlap

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rectangle-overlap/) &nbsp;|&nbsp; **Solved:** 2026-09-14

---

## 📝 Summary

Determine whether two axis-aligned rectangles overlap with a non-zero area.

## 🔍 Key Observation

Two rectangles overlap if and only if their 1D projections overlap on both axes, which is equivalent to ensuring neither rectangle lies completely to the left, right, top, or bottom of the other.

## ⚙️ Algorithm

**Geometry / Interval overlap check**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`geometry` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left1, right1 = min(rec1[0], rec1[2]), max(rec1[0], rec1[2])
        left2, right2 = min(rec2[0], rec2[2]), max(rec2[0], rec2[2])

        bottom1, top1 = min(rec1[1], rec1[3]), max(rec1[1], rec1[3])
        bottom2, top2 = min(rec2[1], rec2[3]), max(rec2[1], rec2[3])

        return not (
            right1 <= left2 or right2 <= left1 or
            top1 <= bottom2 or top2 <= bottom1
        )
```

</details>
