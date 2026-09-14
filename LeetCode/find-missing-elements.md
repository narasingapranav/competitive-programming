# 🟠 find-missing-elements — Find Missing Elements

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-missing-elements/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Accepted solution for Find Missing Elements on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        x=[]
        y=set(nums)
        i=min(nums)
        j=max(nums)+1
        for k in range(i,j):
            if k not in y:
                x.append(k)
        return x

```

</details>
