# 🟠 minimize-manhattan-distances — Minimize Manhattan Distances

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimize-manhattan-distances/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for Minimize Manhattan Distances on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        u = []
        v = []
        for x, y in points:
            u.append(x + y)
            v.append(x - y)
        max_u = max(u)
        min_u = min(u)
        max_v = max(v)
        min_v = min(v)
        second_max_u = sorted(u)[-2]
        second_min_u = sorted(u)[1]
        second_max_v = sorted(v)[-2]
        second_min_v = sorted(v)[1]
        ans = float('inf')
        for i in range(n):
            curr_max_u = second_max_u if u[i] == max_u else max_u
            curr_min_u = second_min_u if u[i] == min_u else min_u
            curr_max_v = second_max_v if v[i] == max_v else max_v
            curr_min_v = second_min_v if v[i] == min_v else min_v
            dist = max(curr_max_u - curr_min_u,
                       curr_max_v - curr_min_v)
            ans = min(ans, dist)
        return ans
```

</details>
