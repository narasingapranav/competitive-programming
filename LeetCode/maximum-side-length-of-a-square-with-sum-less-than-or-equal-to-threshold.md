# 🟠 maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold — Maximum Side Length of a Square with Sum Less than or Equal to Threshold

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) &nbsp;|&nbsp; **Solved:** 2026-01-19

---

## 📝 Summary

Accepted solution for Maximum Side Length of a Square with Sum Less than or Equal to Threshold on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Binary search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`binary-search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

        def possible(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    if ps[i][j] - ps[i - k][j] - ps[i][j - k] + ps[i - k][j - k] <= threshold:
                        return True
            return False

        lo, hi, ans = 0, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
```

</details>
