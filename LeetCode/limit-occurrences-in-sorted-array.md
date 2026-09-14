# 🟠 limit-occurrences-in-sorted-array — Limit Occurrences in Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/limit-occurrences-in-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-05-24

---

## 📝 Summary

Accepted solution for Limit Occurrences in Sorted Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []

        for x in nums:
            n = len(ans)

            # Add element if it appears less than k times
            if n < k or ans[n - k] != x:
                ans.append(x)

        return ans
```

</details>
