# 🟠 next-greater-element-ii — Next Greater Element II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/next-greater-element-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Find the next greater element for each number in a circular array, returning -1 if no greater element exists.

## 🔍 Key Observation

Simulate the circular array by traversing it twice backwards and using a monotonic decreasing stack to maintain candidate next greater elements.

## ⚙️ Algorithm

**Monotonic stack**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`monotonic-stack` `stack` `array` `circular-array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(nums[i%n])
        return res
```

</details>
