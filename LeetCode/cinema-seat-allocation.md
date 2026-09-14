# 🟠 cinema-seat-allocation — Cinema Seat Allocation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Accepted solution for Cinema Seat Allocation on LeetCode.

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
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort(key=lambda x:(x[0],x[1]))
        res=0
        j=0
        for i in range(1,n+1):
            x=0
            while j<len(reservedSeats) and  reservedSeats[j][0]==i:
                x|= 1<<(10-reservedSeats[j][1])
                j+=1
            if x & 480 ==0 :
                if x&30 ==0:
                    res+=2
                else:
                    res+=1
            elif x&120==0:
                res+=1
            elif x&30==0:
                res+=1
            if j==len(reservedSeats):
                res+=(n-i)*2
                break
        return res

```

</details>
