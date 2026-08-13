# 🟠 largest-rectangle-in-histogram — Largest Rectangle in Histogram

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Given an array of integers representing histogram bar heights where each bar has a width of 1, find the area of the largest rectangle that can be formed within the histogram.

## 🔍 Key Observation

The largest rectangle bounded by any bar's height extends left and right until it hits a shorter bar; maintaining an increasing monotonic stack lets us efficiently determine these boundaries in linear time.

## ⚙️ Algorithm

**Monotonic Stack**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`stack` `monotonic-stack` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        st=[]
        i=0
        res=0
        while st or i<n:
            if i<n and (not st or heights[st[-1]]<=heights[i]):
                st.append(i)
                i+=1
            else:
                t=st.pop()
                h=heights[t]
                w= i if not st else i-st[-1]-1
                res=max(res,h*w)
        return res
```

</details>
