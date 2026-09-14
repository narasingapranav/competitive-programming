# 🟠 jump-game-ix — Jump Game IX

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-ix/) &nbsp;|&nbsp; **Solved:** 2026-05-07

---

## 📝 Summary

Accepted solution for Jump Game IX on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        suf = [0] * n
        res = [0] * n

        # prefix max
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])

        # suffix min
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        res[-1] = pre[-1]

        # build answer
        for i in range(n - 2, -1, -1):

            # merge segment
            if pre[i] > suf[i + 1]:
                res[i] = res[i + 1]

            # new segment
            else:
                res[i] = pre[i]

        return res
```

</details>
