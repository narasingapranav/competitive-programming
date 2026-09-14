# 🟠 jump-game-vii — Jump Game VII

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-vii/) &nbsp;|&nbsp; **Solved:** 2026-05-25

---

## 📝 Summary

Accepted solution for Jump Game VII on LeetCode.

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
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                reachable += 1

            if i > maxJump and dp[i - maxJump - 1]:
                reachable -= 1

            if reachable > 0 and s[i] == '0':
                dp[i] = True

        return dp[-1]
```

</details>
