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
        n = len(nums)
        ans = 0
        for i in range(n):
            even_set = set()
            odd_set = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                if len(even_set) == len(odd_set):
                    ans = max(ans, j - i + 1)
        return ans
```

</details>
