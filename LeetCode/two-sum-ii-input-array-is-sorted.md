# 🟠 two-sum-ii-input-array-is-sorted — Two Sum II - Input Array Is Sorted

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) &nbsp;|&nbsp; **Solved:** 2026-07-22

---

## 📝 Summary

Accepted solution for Two Sum II - Input Array Is Sorted on LeetCode.

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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        while low<high:
            if nums[low]+nums[high]>target:
                high-=1
            elif nums[low]+nums[high]==target:
                return [low+1,high+1]
            else:
                low+=1
```

</details>
