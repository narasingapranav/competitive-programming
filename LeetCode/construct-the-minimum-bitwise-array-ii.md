# 🟠 construct-the-minimum-bitwise-array-ii — Construct the Minimum Bitwise Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-01-21

---

## 📝 Summary

Accepted solution for Construct the Minimum Bitwise Array II on LeetCode.

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
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num == 2:
                result.append(-1)
            else:
                leadingOne = 1
                while (num & leadingOne) > 0:
                    leadingOne <<= 1
                result.append(num - (leadingOne >> 1))
        return result
```

</details>
