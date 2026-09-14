# 🟠 find-the-number-of-subsequences-with-equal-gcd — Find the Number of Subsequences With Equal GCD

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/) &nbsp;|&nbsp; **Solved:** 2026-07-14

---

## 📝 Summary

Accepted solution for Find the Number of Subsequences With Equal GCD on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp` `recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    '''
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    '''
    def subsequencePairCount(self, nums: List[int]) -> int:
        @cache
        def dfs(i, a, b):
            if i == len(nums):
                return 1 if a == b else 0
            return (
                dfs(i + 1, a, b) +  # do not take 
                dfs(i + 1, gcd(a, nums[i]), b) +  # take into A
                dfs(i + 1, a, gcd(b, nums[i]))  # take into B
            ) % (10 ** 9 + 7)
        return dfs(0, 0, 0) - 1  # exclude the one case to take nothing
```

</details>
