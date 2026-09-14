# 🟠 minimum-pair-removal-to-sort-array-i — Minimum Pair Removal to Sort Array I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/) &nbsp;|&nbsp; **Solved:** 2026-01-01

---

## 📝 Summary

Accepted solution for Minimum Pair Removal to Sort Array I on LeetCode.

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
  def minimumPairRemoval(self, nums: list[int]) -> int:
    ans = 0
    while any(x > y for x, y in itertools.pairwise(nums)):
      pairSums = [x + y for x, y in itertools.pairwise(nums)]
      minPairSum = min(pairSums)
      minPairIndex = pairSums.index(minPairSum)
      nums[minPairIndex] = minPairSum
      nums.pop(minPairIndex + 1)
      ans += 1

    return ans
```

</details>
