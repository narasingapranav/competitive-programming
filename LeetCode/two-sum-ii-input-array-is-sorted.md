# 🟠 two-sum-ii-input-array-is-sorted — Two Sum II - Input Array Is Sorted

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) &nbsp;|&nbsp; **Solved:** 2025-12-10

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
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        while l!=r:
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                return [l+1,r+1]
```

</details>
