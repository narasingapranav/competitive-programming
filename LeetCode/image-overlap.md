# 🟠 image-overlap — Image Overlap

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/image-overlap/) &nbsp;|&nbsp; **Solved:** 2026-09-13

---

## 📝 Summary

Find the maximum possible count of overlapping 1s between two binary matrices when one matrix is translated in any direction over the other.

## 🔍 Key Observation

A translation vector (row offset, column offset) maps a 1 in the first matrix to a 1 in the second matrix; the vector that appears most frequently across all pairs of 1s corresponds to the optimal shift.

## ⚙️ Algorithm

**Hash Map / Translation Vector Counting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N^4)` | `O(N^2)` |

## 🏷️ Tags

`matrix` `hash-map` `counting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        pos1 = []
        pos2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    pos1.append((i, j))
                if img2[i][j] == 1:
                    pos2.append((i, j))

        res = 0
        mp = {}

        for p1 in pos1:
            for p2 in pos2:
                r = p2[0] - p1[0]
                c = p2[1] - p1[1]

                key = (r, c)
                mp[key] = mp.get(key, 0) + 1

                res = max(res, mp[key])

        return res
```

</details>
