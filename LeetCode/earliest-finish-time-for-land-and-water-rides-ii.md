# 🟠 earliest-finish-time-for-land-and-water-rides-ii — Earliest Finish Time for Land and Water Rides II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/) &nbsp;|&nbsp; **Solved:** 2026-06-03

---

## 📝 Summary

Accepted solution for Earliest Finish Time for Land and Water Rides II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def earliestFinishTime(
        self, la: list[int], lb: list[int], wa: list[int], wb: list[int]
    ) -> int:
        MAX = 300005
        l = w = minL = minW = MAX
        n, m = len(la), len(wa)

        for i in range(n):
            l = min(l, la[i] + lb[i])

        for i in range(m):
            w = min(w, wa[i] + wb[i])
            minL = min(minL, max(wa[i], l) + wb[i])

        for i in range(n):
            minW = min(minW, max(la[i], w) + lb[i])

        return min(minW, minL)
```

</details>
