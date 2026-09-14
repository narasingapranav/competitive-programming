# 🟠 divide-an-array-into-subarrays-with-minimum-cost-ii — Divide an Array Into Subarrays With Minimum Cost II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-02

---

## 📝 Summary

Accepted solution for Divide an Array Into Subarrays With Minimum Cost II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Binary search + Two pointers + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`binary-search` `sorting`

<details>
<summary>💻 View solution</summary>

```python
from bisect import bisect_left, bisect_right

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # Restart the problem
        first = nums[0]
        nums = nums[1:]
        k -= 1
        # Solve the sliding window problem
        # Start with leftmost window
        window = nums[:dist+1]
        window.sort()
        best = curr = sum(window[:k])
        # Slide window to the right
        for i in range(dist+1, len(nums)):
            # Remove the left item from the old window
            old = nums[i-dist-1]
            old_idx = bisect_left(window, old)
            del window[old_idx]
            if old_idx < k:
                curr -= old
                if len(window) > k-1:
                    curr += window[k-1]
            # Add the right item from the new window
            new = nums[i]
            new_idx = bisect_right(window, new)
            window.insert(new_idx, new)
            if new_idx < k:
                curr += new
                if len(window) > k:
                    curr -= window[k]
            # Update best
            if curr < best:
                best = curr
        return best + first
```

</details>
