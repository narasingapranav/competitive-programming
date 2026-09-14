# 🟠 trionic-array-ii — Trionic Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/trionic-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-05

---

## 📝 Summary

Accepted solution for Trionic Array II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        res = -float('inf')
        i = 1
        while i < n - 2:
            a = b = i
            net = nums[a]
            while b + 1 < n and nums[b + 1] < nums[b]:
                net += nums[b + 1]
                b += 1
            if b == a:
                i += 1
                continue
            
            c = b
            left = right = 0
            lx = rx = -float('inf')
            
            while a - 1 >= 0 and nums[a - 1] < nums[a]:
                left += nums[a - 1]
                lx = max(lx, left)
                a -= 1
            if a == i:
                i += 1
                continue
            
            while b + 1 < n and nums[b + 1] > nums[b]:
                right += nums[b + 1]
                rx = max(rx, right)
                b += 1
            if b == c:
                i += 1
                continue
                
            res = max(res, lx + rx + net)
            i = b
        return res if res != -float('inf') else 0
```

</details>
