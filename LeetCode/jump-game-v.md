# 🟠 jump-game-v — Jump Game V

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-v/) &nbsp;|&nbsp; **Solved:** 2026-05-24

---

## 📝 Summary

Accepted solution for Jump Game V on LeetCode.

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
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def solveMem(i):
            if dp[i] != -1:
                return dp[i]

            ans = 1

            # move right
            for j in range(i + 1, min(i + d, n - 1) + 1):
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + solveMem(j))

            # move left
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + solveMem(j))

            dp[i] = ans
            return dp[i]

        ans = 1

        for i in range(n):
            ans = max(ans, solveMem(i))

        return ans
```

</details>
