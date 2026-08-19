# 🟠 cherry-pickup — Cherry Pickup

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/cherry-pickup/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Find the maximum number of cherries that can be collected by making a round trip between the top-left and bottom-right corners of an N x N grid containing cherries, empty cells, and obstacles.

## 🔍 Key Observation

A round trip from start to end and back is equivalent to two people walking simultaneously from (0,0) to (N-1,N-1) taking right and down steps, where cherries at the same grid cell are counted only once if both reach it at the same step.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N^3)` | `O(N^2)` |

## 🏷️ Tags

`dynamic-programming` `grid`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int cherryPickup(int[][] grid) {
        int n=grid.length;int m=2*n-1;
        int dp[][]=new int[n][n];
        dp[0][0]=grid[0][0];
        for(int k=1;k<m;k++){
            for(int i=n-1;i>=0;i--){
                for(int j=n-1;j>=0;j--){
                    int p=k-i,q=k-j;
                    if(p<0||p>=n||q<0||q>=n||grid[i][p]<0||grid[j][q]<0){
                        dp[i][j]=-1;continue;
                    }
                    if(i>0)dp[i][j]=Math.max(dp[i][j],dp[i-1][j]);
                    if(j>0)dp[i][j]=Math.max(dp[i][j],dp[i][j-1]);
                    if(i>0&&j>0)dp[i][j]=Math.max(dp[i][j],dp[i-1][j-1]);
                    if(dp[i][j]>=0)dp[i][j]+=grid[i][p]+((i!=j)?grid[j][q]:0);
                   
                }
            }
        }
        return dp[n-1][n-1]>=0?dp[n-1][n-1]:0;
    }
}
```

</details>
