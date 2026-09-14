# 🟠 container-with-most-water — Container With Most Water

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/container-with-most-water/) &nbsp;|&nbsp; **Solved:** 2026-07-22

---

## 📝 Summary

Accepted solution for Container With Most Water on LeetCode.

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
    def maxArea(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        area=0
        max_area=0
        while low<=high:
            area=min(height[low],height[high])*(high-low)
            max_area=max(area,max_area)
            if height[low]<height[high]:
                low+=1
            else:
                high-=1
        return max_area
```

</details>
