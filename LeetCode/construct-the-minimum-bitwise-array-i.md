# 🟠 construct-the-minimum-bitwise-array-i — Construct the Minimum Bitwise Array I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/) &nbsp;|&nbsp; **Solved:** 2026-01-20

---

## 📝 Summary

Accepted solution for Construct the Minimum Bitwise Array I on LeetCode.

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
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                for i in range(1, 32):
                    if ((x >> i) & 1) == 0:
                        ans.append(x ^ (1 << (i - 1)))
                        break
        return ans
```

</details>
