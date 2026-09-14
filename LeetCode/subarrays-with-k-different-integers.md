# 🟠 subarrays-with-k-different-integers — Subarrays with K Different Integers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Accepted solution for Subarrays with K Different Integers on LeetCode.

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
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums, k):
        freq = defaultdict(int)
        left = 0
        count = 0
        distinct = 0

        for right in range(len(nums)):
            # include nums[right]
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            # shrink window if too many distinct
            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            # all subarrays ending at 'right'
            count += right - left + 1

        return count

```

</details>
