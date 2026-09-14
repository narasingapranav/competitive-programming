# 🟠 stone-game-iii — Stone Game III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game-iii/) &nbsp;|&nbsp; **Solved:** 2026-08-29

---

## 📝 Summary

Accepted solution for Stone Game III on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    s = ["Bob", "Tie", "Alice"]
    def stoneGameIII(self, A: List[int]) -> str:
        n = len(A)
        @cache
        def maxDiff(i: int) -> int:
            if i == n: return 0
            a = b = c = -5e7
            if i < n:
                a = A[i] - maxDiff(i + 1)
            if i + 1 < n:
                b = A[i] + A[i + 1] - maxDiff(i + 2)
            if i + 2 < n:
                c = A[i] + A[i + 1] + A[i + 2] - maxDiff(i + 3)
            return max(a, b, c)
        d = maxDiff(0)
        return self.s[(d > 0) - (d < 0) + 1]
```

</details>
