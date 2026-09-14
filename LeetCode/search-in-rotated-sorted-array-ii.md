# 🟠 search-in-rotated-sorted-array-ii — Search in Rotated Sorted Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-09

---

## 📝 Summary

Determine whether a given target integer exists in a sorted array that has been rotated and may contain duplicate elements.

## 🔍 Key Observation

Because duplicates can cause ambiguity during binary search pivots, the worst-case time complexity degrades to O(n), making a linear scan sufficient for correctness and efficiency within worst-case bounds.

## ⚙️ Algorithm

**Linear Search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`array` `search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
```

</details>
