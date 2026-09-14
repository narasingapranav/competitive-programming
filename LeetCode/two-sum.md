# 🟠 two-sum — Two Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/two-sum/) &nbsp;|&nbsp; **Solved:** 2026-06-30

---

## 📝 Summary

Accepted solution for Two Sum on LeetCode.

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
    def twoSum(self,arr,k):
        dic={}
        for i , num in enumerate(arr):
            c=k-num
            if c in dic:
                return [dic[c],i]
            dic[num]=i
```

</details>
