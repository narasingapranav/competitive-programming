# 🟠 valid-binary-strings-with-cost-limit — Valid Binary Strings With Cost Limit

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/valid-binary-strings-with-cost-limit/) &nbsp;|&nbsp; **Solved:** 2026-06-07

---

## 📝 Summary

Accepted solution for Valid Binary Strings With Cost Limit on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []

        def dfs(i: int, cost: int, prev_one: bool, path: list):
            if cost > k:
                return

            if i == n:
                ans.append("".join(path))
                return

            # Place '0'
            path.append('0')
            dfs(i + 1, cost, False, path)
            path.pop()

            # Place '1'
            if not prev_one and cost + i <= k:
                path.append('1')
                dfs(i + 1, cost + i, True, path)
                path.pop()

        dfs(0, 0, False, [])
        return ans
```

</details>
