# 🟠 minimum-energy-to-maintain-brightness — Minimum Energy to Maintain Brightness

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-energy-to-maintain-brightness/) &nbsp;|&nbsp; **Solved:** 2026-06-07

---

## 📝 Summary

Accepted solution for Minimum Energy to Maintain Brightness on LeetCode.

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
  def minEnergy(self, n: int, brightness: int,
                intervals: list[list[int]]) -> int:

    intervals.sort()
    time, (beg, end) = 0, intervals[0]

    for left, rght in intervals:
        
      if end < left:   # disjoint intervals
        time+= end - beg + 1
        beg, end = left, rght

      elif end < rght: # overlapping intervals
        end = rght

    return ceil(brightness/3) * (time + end - beg + 1)
  
```

</details>
