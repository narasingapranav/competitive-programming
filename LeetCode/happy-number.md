# 🟠 happy-number — Happy Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/happy-number/) &nbsp;|&nbsp; **Solved:** 2025-08-15

---

## 📝 Summary

Accepted solution for Happy Number on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=1 and n not in s:
            s.add(n)
            sum=0
            while n>0:
                rem=n%10
                sum+=rem**2
                n//=10
            n=sum
        return n==1
```

</details>
