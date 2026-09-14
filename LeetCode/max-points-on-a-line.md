# 🟠 max-points-on-a-line — Max Points on a Line

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/max-points-on-a-line/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for Max Points on a Line on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    '''def slope(self,p1,p2):
        x1,y1=p1
        x2,y2=p2
        if abs(x2-x1) ==0:
            return 1
        return (y2-y1)/(x2-x1)'''
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <=2:
            return len(points)
        maxi=2
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                counter=2
                for k in range(j+1,len(points)):
                    s1=(points[j][1]-points[i][1] )* (points[k][0]-points[i][0])
                    s2=(points[k][1]-points[i][1]) * (points[j][0]-points[i][0])
                    if s1==s2:
                        counter+=1
                maxi=max(maxi,counter)
        return maxi
```

</details>
