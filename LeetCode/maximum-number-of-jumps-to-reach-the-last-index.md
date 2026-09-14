# 🟠 maximum-number-of-jumps-to-reach-the-last-index — Maximum Number of Jumps to Reach the Last Index

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) &nbsp;|&nbsp; **Solved:** 2026-05-10

---

## 📝 Summary

Accepted solution for Maximum Number of Jumps to Reach the Last Index on LeetCode.

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
    def maximumJumps(self, nums, target):

        n = len(nums)

        # dp[i] stores maximum jumps to reach index i
        dp = [-1] * n

        # Starting index needs 0 jumps
        dp[0] = 0

        for i in range(1, n):

            # Check all previous indices
            for j in range(i):

                # Valid jump and previous index reachable
                if abs(nums[i] - nums[j]) <= target and dp[j] != -1:

                    # Update maximum jumps
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]
```

</details>
