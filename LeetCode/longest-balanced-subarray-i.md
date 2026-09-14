# 🟠 longest-balanced-subarray-i — Longest Balanced Subarray I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-balanced-subarray-i/) &nbsp;|&nbsp; **Solved:** 2026-02-10

---

## 📝 Summary

Accepted solution for Longest Balanced Subarray I on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        best = 0
        balance = tuple([set(), set()])
        while len(nums) > best:
            balance[0].clear(); balance[1].clear()
            for r, x in enumerate(reversed(nums), start=1):
                balance[x & 1].add(x)
                if len(balance[0]) == len(balance[1]):
                    best = max(best, r)
            nums.pop()
        return best
```

</details>
