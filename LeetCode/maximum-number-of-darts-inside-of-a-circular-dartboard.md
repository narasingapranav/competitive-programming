# 🟠 maximum-number-of-darts-inside-of-a-circular-dartboard — Maximum Number of Darts Inside of a Circular Dartboard

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for Maximum Number of Darts Inside of a Circular Dartboard on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
import math
class Solution:
    def countutility(self,cX,cY,r,darts):
        count = 0
        for x, y in darts:
            if (x - cX) ** 2 + (y - cY) ** 2 <= r * r + 1e-7:
                count += 1
        return count
    def computeutility(self,darts,dart,r,maxdarts):
        n=len(darts)
        for i in range(360):
            if maxdarts==n:
                return n
            angle=math.radians(i)
            cX=dart[0]+ r * math.cos(angle)
            cY=dart[1]+ r * math.sin(angle)
            counter=self.countutility(cX,cY,r,darts)
            if counter>maxdarts:
                maxdarts=counter
        return maxdarts
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        maxdarts=0
        n=len(darts)
        for i in range(n):
            maxdarts=max(maxdarts,self.computeutility(darts, darts[i], r, maxdarts))
        return maxdarts
```

</details>
