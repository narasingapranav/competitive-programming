# 🟠 left-and-right-sum-differences — Left and Right Sum Differences

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/) &nbsp;|&nbsp; **Solved:** 2026-06-06

---

## 📝 Summary

Accepted solution for Left and Right Sum Differences on LeetCode.

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
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightSum = sum(nums)
        leftSum = 0
        ans = []
        for num in nums:
            rightSum -= num
            ans.append(abs(leftSum - rightSum))
            leftSum += num
        return ans
```

</details>
