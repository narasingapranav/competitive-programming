# 🟠 unique-paths-ii — Unique Paths II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-paths-ii/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Accepted solution for Unique Paths II on LeetCode.

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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        for i in range(1,len(obstacleGrid)):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]
        for i in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][i]==0:
                dp[0][i]=dp[0][i-1]
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0
        return dp[-1][-1]

```

</details>
