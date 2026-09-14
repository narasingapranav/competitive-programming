# 🟠 permutations-ii — Permutations II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/permutations-ii/) &nbsp;|&nbsp; **Solved:** 2025-12-09

---

## 📝 Summary

Accepted solution for Permutations II on LeetCode.

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
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        res = []

        for n in nums:
            counts[n] += 1
        
        def helper(sub, counts):

            if len(sub) == len(nums):
                res.append(sub[::])
                return

            for n in counts:

                if counts[n] == 0:
                    continue
                
                counts[n] -= 1
                sub.append(n)

                helper(sub, counts)

                sub.pop()
                counts[n] += 1
        
        helper([], counts)
        return res

```

</details>
