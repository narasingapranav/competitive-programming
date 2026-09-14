# 🟠 stone-game-viii — Stone Game VIII

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game-viii/) &nbsp;|&nbsp; **Solved:** 2026-08-24

---

## 📝 Summary

Accepted solution for Stone Game VIII on LeetCode.

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
    def stoneGameVIII(self, stones):
        n = len(stones)

        prefix = stones[:]

        # Build prefix sums
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        # If Alice takes all stones,
        # the game ends immediately.
        best = prefix[n - 1]

        # Try every earlier valid prefix
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)

        return best
```

</details>
