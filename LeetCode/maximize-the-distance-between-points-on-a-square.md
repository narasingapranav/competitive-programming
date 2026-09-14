# 🟠 maximize-the-distance-between-points-on-a-square — Maximize the Distance Between Points on a Square

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/) &nbsp;|&nbsp; **Solved:** 2026-04-25

---

## 📝 Summary

Accepted solution for Maximize the Distance Between Points on a Square on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Binary search + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`binary-search` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def flatten(p):
            x, y = p
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y
        arr = sorted(flatten(p) for p in points)
        n = len(arr)
        def notValid(d):
            for i in range(n):
                ptr = i
                cnt = 1
                while cnt < k:
                    target = arr[ptr] + d
                    import bisect
                    j = bisect.bisect_left(arr, target)
                    if j == n:
                        break
                    ptr = j
                    cnt += 1
                    if d + arr[ptr] > arr[i] + 4 * side:
                        cnt = 0
                        break
                if cnt == k:
                    return False
            return True
        low, high = 0, side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if not notValid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
```

</details>
