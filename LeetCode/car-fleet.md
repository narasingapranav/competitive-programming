# 🟠 car-fleet — Car Fleet

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/car-fleet/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Accepted solution for Car Fleet on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(speed)
        car=[]
        for i,j in zip(position,speed):
            car.append((i,(target-i)/j))
        car.sort(key=lambda x:x[0],reverse=True)
        c=1
        t=car[0][1]
        for i in range(1,n):
            if car[i][1]>t:
                c+=1
                t=car[i][1]
        return c
```

</details>
