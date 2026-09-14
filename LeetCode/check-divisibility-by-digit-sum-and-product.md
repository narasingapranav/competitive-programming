# 🟠 check-divisibility-by-digit-sum-and-product — Check Divisibility by Digit Sum and Product

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/) &nbsp;|&nbsp; **Solved:** 2026-08-22

---

## 📝 Summary

Accepted solution for Check Divisibility by Digit Sum and Product on LeetCode.

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
    def checkDivisibility(self, n: int) -> bool:
        n_str=str(n)
        prod=1
        su=0
        for i in n_str:
            prod*=int(i)
            su+=int(i)   
        return n%(prod+su)==0    


        
```

</details>
