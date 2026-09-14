class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        m=len(grid)
        n=len(grid[0])
        vis=[[False]*n for _ in range(m)]
        def dfs(i,j):
            if i>=m or j>=n or i <0 or j<0 or vis[i][j] or grid[i][j]=='0':
                return 
            vis[i][j]=True
            dirs=[(0,-1),(0,1),(-1,0),(1,0)]
            for di,dj in dirs:
                ni,nj=i+di,j+dj
                dfs(ni,nj)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not vis[i][j]:
                    dfs(i,j)
                    count+=1
        return count