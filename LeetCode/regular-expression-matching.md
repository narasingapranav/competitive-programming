# 🟠 regular-expression-matching — Regular Expression Matching

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/regular-expression-matching/) &nbsp;|&nbsp; **Solved:** 2025-08-24

---

## 📝 Summary

Accepted solution for Regular Expression Matching on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # Get lengths of text and pattern
        text_length, pattern_length = len(text), len(pattern)

        # Initialize DP table with False values
        dp = [[False] * (pattern_length + 1) for _ in range(text_length + 1)]

        # Empty pattern matches an empty text
        dp[0][0] = True

        # Iterate over text and pattern lengths
        for i in range(text_length + 1):
            for j in range(1, pattern_length + 1):
                # If the pattern character is '*', it could match zero or more of the previous element
                if pattern[j - 1] == "*":
                    # Check if zero occurrences of the character before '*' match
                    dp[i][j] = dp[i][j - 2]
                    # Additional check for one or more occurrences    
                    if i > 0 and (pattern[j - 2] == "." or text[i - 1] == pattern[j - 2]):
                        dp[i][j] |= dp[i - 1][j]
                # If the current characters match or if pattern has '.', mark as true
                elif i > 0 and (pattern[j - 1] == "." or text[i - 1] == pattern[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]

        # The result is at the bottom right of the DP table
        return dp[text_length][pattern_length]
```

</details>
