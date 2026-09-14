# 🟠 course-schedule-iii — Course Schedule III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/course-schedule-iii/) &nbsp;|&nbsp; **Solved:** 2026-02-28

---

## 📝 Summary

Accepted solution for Course Schedule III on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key= lambda x:(x[1],x[0]))
        tt=0
        nc=0
        q=[]
        for d,ld in courses:
            tt+=d
            heapq.heappush(q,-d)
            if tt>ld:
                tt-= -heapq.heappop(q)
        return len(q)
```

</details>
