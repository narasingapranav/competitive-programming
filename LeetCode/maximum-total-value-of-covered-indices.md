# 🟠 maximum-total-value-of-covered-indices — Maximum Total Value of Covered Indices

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-total-value-of-covered-indices/) &nbsp;|&nbsp; **Solved:** 2026-06-06

---

## 📝 Summary

Accepted solution for Maximum Total Value of Covered Indices on LeetCode.

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
    def maxTotal(self, nums: List[int], s: str) -> int:
        pos = [i for i, ch in enumerate(s) if ch == '1']

        if not pos:
            return 0

        NEG = -10**18

        # dp[pos occupied by previous token]
        dp = {}

        first = pos[0]

        if first == 0:
            dp[0] = nums[0]
        else:
            dp[first - 1] = nums[first - 1]
            dp[first] = nums[first]

        for p in pos[1:]:
            ndp = {}

            for last_pos, cur in dp.items():

                for final_pos in ([p] if p == 0 else [p - 1, p]):
                    add = nums[final_pos]

                    if final_pos == last_pos:
                        add = 0

                    ndp[final_pos] = max(
                        ndp.get(final_pos, NEG),
                        cur + add
                    )

            dp = ndp

        return max(dp.values())
```

</details>
