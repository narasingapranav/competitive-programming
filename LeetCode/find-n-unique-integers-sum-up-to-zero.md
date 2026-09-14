# 🟠 find-n-unique-integers-sum-up-to-zero — Find N Unique Integers Sum up to Zero

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) &nbsp;|&nbsp; **Solved:** 2025-09-07

---

## 📝 Summary

Accepted solution for Find N Unique Integers Sum up to Zero on LeetCode.

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
    def sumZero(self, n: int) -> List[int]:
        res=[]
        for i in range(1,n//2 +1):
            res.append(i)
            res.append(-i)
        if n%2!=0:
            res.append(0)
        return res
```

</details>
