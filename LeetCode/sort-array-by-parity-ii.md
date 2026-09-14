# 🟠 sort-array-by-parity-ii — Sort Array By Parity II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sort-array-by-parity-ii/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Accepted solution for Sort Array By Parity II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i%2==0:
                p.append(i)
            else:
                n.append(i)
        a=[]
        for i,j in zip(range(len(p)),range(len(n))):
            a.append(p[i])
            a.append(n[j])
        return a
```

</details>
