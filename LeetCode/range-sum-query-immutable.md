# 🟠 range-sum-query-immutable — Range Sum Query - Immutable

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/range-sum-query-immutable/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Range Sum Query - Immutable on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Two pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0] * (len(nums)+1)
        self.prefix[0] = nums[0]

        for idx, num in enumerate(nums):
            self.prefix[idx+1] = self.prefix[idx] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

</details>
