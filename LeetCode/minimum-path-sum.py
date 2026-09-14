class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        dp=[[0]*c for i in range(r)]
        dp[0][0]=grid[0][0]
        for a in range(1,r):
            dp[a][0]=dp[a-1][0]+grid[a][0]
        for b in range(1,c):
            dp[0][b]=dp[0][b-1]+grid[0][b]
        for a in range(1,r):
            for b in range(1,c):
                dp[a][b]=min(dp[a-1][b],dp[a][b-1])+grid[a][b]
        return dp[-1][-1]
         