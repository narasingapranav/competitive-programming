# 🟠 kth-missing-positive-number — Kth Missing Positive Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/kth-missing-positive-number/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Accepted solution for Kth Missing Positive Number on LeetCode.

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
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m=0
        c=1
        i=0
        while m<k:
            if i<len(arr) and arr[i]==c:
                i+=1
            else:
                m+=1
                if m==k:
                    return c
            c+=1
```

</details>
