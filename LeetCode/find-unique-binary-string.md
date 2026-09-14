# 🟠 find-unique-binary-string — Find Unique Binary String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-unique-binary-string/) &nbsp;|&nbsp; **Solved:** 2026-03-08

---

## 📝 Summary

Accepted solution for Find Unique Binary String on LeetCode.

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
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        ans=['0']*n
        for i, x in enumerate(nums):
            if x[i]=='0':
                ans[i]='1'
            else:
                ans[i]='0'
        return "".join(ans)
                
```

</details>
