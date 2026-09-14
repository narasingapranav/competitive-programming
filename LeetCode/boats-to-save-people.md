# 🟠 boats-to-save-people — Boats to Save People

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/boats-to-save-people/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Accepted solution for Boats to Save People on LeetCode.

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
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # l=0
        # n=len(people)
        # boats=[]
        # r=1
        # while r<n:
        #     w=people[l:r]
        #     if sum(w)>limit:
        #         boats.append(w)
        #         l+=1
        #         r+=1
        #     else:
        #         boats.append(w)
        #         l+=2
        #         r+=2
        # return boats
        people.sort()
        l,r=0,len(people)-1
        boats=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            boats+=1
        return boats
```

</details>
