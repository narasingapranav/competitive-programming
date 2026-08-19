# 🟠 delete-operation-for-two-strings — Delete Operation for Two Strings

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Find the minimum number of character deletions required to make two strings identical.

## 🔍 Key Observation

The problem can be modeled as finding the minimum deletion edit distance, which is closely related to finding the Longest Common Subsequence (LCS) between the two strings.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n)` | `O(m * n)` |

## 🏷️ Tags

`dynamic-programming` `string` `lcs` `edit-distance`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1==word2:
            return 0
        if len(word1)==len(word2)==1:
            return 2
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
        return dp[m][n]
```

</details>
