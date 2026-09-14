# 🟠 count-subarrays-with-majority-element-ii — Count Subarrays With Majority Element II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-ii/) &nbsp;|&nbsp; **Solved:** 2026-06-26

---

## 📝 Summary

Accepted solution for Count Subarrays With Majority Element II on LeetCode.

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
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = n

        freq = [0] * (2 * n + 1)
        freq[n] = 1

        less = 0
        ans = 0

        for num in nums:
            if num == target:
                less += freq[pref]
                pref += 1
            else:
                pref -= 1
                less -= freq[pref]

            freq[pref] += 1
            ans += less

        return ans
```

</details>
