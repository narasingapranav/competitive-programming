# 🟠 maximum-value-of-an-alternating-sequence — Maximum Value of an Alternating Sequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Accepted solution for Maximum Value of an Alternating Sequence on LeetCode.

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
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        # res=[s]
        # if n>1:
        #     ans=s+m
        #     res.append(ans)
        #     i=2
        #     while i<n:
        #         if i&1:
        #             res.append(res[i-1]+m)
        #         else:
        #             res.append(res[i-1]-1)
        #         i+=1
        #     return max(res)
        pk=n//2
        return s+pk*m-(pk-1)
```

</details>
