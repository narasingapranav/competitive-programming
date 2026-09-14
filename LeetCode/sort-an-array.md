# 🟠 sort-an-array — Sort an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sort-an-array/) &nbsp;|&nbsp; **Solved:** 2025-12-18

---

## 📝 Summary

Accepted solution for Sort an Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^6) (estimated -- 6 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countingSort(self, nums, exp):
        n = len(nums)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (nums[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            output[count[index] - 1] = nums[i]
            count[index] -= 1
        for i in range(n):
            nums[i] = output[i]
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        neg = [-x for x in nums if x < 0]
        pos = [x for x in nums if x >= 0]

        if neg:
            max_neg = max(neg)
            exp = 1
            while max_neg // exp > 0:
                self.countingSort(neg, exp)
                exp *= 10

        if pos:
            max_pos = max(pos)
            exp = 1
            while max_pos // exp > 0:
                self.countingSort(pos, exp)
                exp *= 10

        neg = [-x for x in reversed(neg)]
        return neg + pos

```

</details>
