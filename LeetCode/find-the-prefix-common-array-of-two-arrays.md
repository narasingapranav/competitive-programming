# 🟠 find-the-prefix-common-array-of-two-arrays — Find the Prefix Common Array of Two Arrays

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) &nbsp;|&nbsp; **Solved:** 2026-05-20

---

## 📝 Summary

Accepted solution for Find the Prefix Common Array of Two Arrays on LeetCode.

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
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[0]*n
        seen=[0]*(n+1)
        for i in range(n):
            seen[0]+=seen[A[i]]
            seen[A[i]]=1
            seen[0]+=seen[B[i]]
            seen[B[i]]=1
            res[i]=seen[0]
        return res
```

</details>
