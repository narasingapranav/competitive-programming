# 🟠 count-indices-with-opposite-parity — Count Indices With Opposite Parity

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-indices-with-opposite-parity/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for Count Indices With Opposite Parity on LeetCode.

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
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd=even=0
        res=[]
        for i in reversed(nums):
            if i%2==0:
                even+=1
                res.append(odd)
            else:
                odd+=1
                res.append(even)
        return res[::-1]
```

</details>
