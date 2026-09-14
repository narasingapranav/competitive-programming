# 🟠 k-closest-points-to-origin — K Closest Points to Origin

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for K Closest Points to Origin on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k==len(points):
            return points
        points.sort(key=lambda p : p[0]*p[0] + p[1]*p[1])
        return points[:k]

```

</details>
