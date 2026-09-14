# 🟠 earliest-finish-time-for-land-and-water-rides-i — Earliest Finish Time for Land and Water Rides I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/) &nbsp;|&nbsp; **Solved:** 2026-06-02

---

## 📝 Summary

Accepted solution for Earliest Finish Time for Land and Water Rides I on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def earliestFinishTime(self,landStartTime: List[int],landDuration: List[int],waterStartTime: List[int],waterDuration: List[int]) -> int:
        res = float('inf')
        n, m = len(landStartTime), len(waterStartTime)

        for i in range(n):  # loop over all land rides
            a, d = landStartTime[i], landDuration[i]  # a = start, d = duration of land ride
            for j in range(m):  # loop over all water rides
                b, e = waterStartTime[j], waterDuration[j]  # b = start, e = duration of water ride

                # Land → Water
                land_end = a + d
                start_water = max(land_end, b)
                finish1 = start_water + e

                # Water → Land
                water_end = b + e
                start_land = max(water_end, a)
                finish2 = start_land + d

                # Take the minimum of all finish times
                res = min(res, finish1, finish2)

        return res
```

</details>
