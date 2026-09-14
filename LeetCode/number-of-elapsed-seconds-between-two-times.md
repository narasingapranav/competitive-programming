# 🟠 number-of-elapsed-seconds-between-two-times — Number of Elapsed Seconds Between Two Times

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Accepted solution for Number of Elapsed Seconds Between Two Times on LeetCode.

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
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st=list(map(int,startTime.split(":")))
        et=list(map(int,endTime.split(":")))
        res=[]
        for i in range(len(st)):
            res.append(et[i]-st[i])
        return res[0]*3600+res[1]*60+res[2]
```

</details>
