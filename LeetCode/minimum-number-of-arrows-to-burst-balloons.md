# 🟠 minimum-number-of-arrows-to-burst-balloons — Minimum Number of Arrows to Burst Balloons

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Accepted solution for Minimum Number of Arrows to Burst Balloons on LeetCode.

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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        end=points[0][1]
        count=1
        for s,e in points:
            if s>end:
                count+=1
                end=e
        return count
```

</details>
