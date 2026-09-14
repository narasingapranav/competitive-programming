# 🟠 container-with-most-water — Container With Most Water

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/container-with-most-water/) &nbsp;|&nbsp; **Solved:** 2026-07-01

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
        l=0
        r=len(height)-1
        a=0
        m=0
        while l<r:
            a=min(height[l],height[r])*(r-l)
            m=max(a,m)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m
                

```

</details>
