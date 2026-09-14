# 🟠 unique-3-digit-even-numbers — Unique 3-Digit Even Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/) &nbsp;|&nbsp; **Solved:** 2025-12-14

---

## 📝 Summary

Accepted solution for Unique 3-Digit Even Numbers on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=set()
        n=len(digits)
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range(n):
                if i==j:
                    continue 
                for k in range(n):
                    if k==i or k==j:
                        continue 
                    if digits[k]%2==0:
                        a=digits[i]*100+digits[j]*10+digits[k]
                        s.add(a)
        return len(s)
```

</details>
