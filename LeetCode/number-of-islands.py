class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        def dfs(r,c):
            d=[(1,0),(-1,0),(0,1),(0,-1)]
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return
            if visited[r][c] or grid[r][c]=='0':
                return
            visited[r][c]=True
            for dr,dc in d:
                dfs(r+dr,c+dc)
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and not visited[i][j]:
                    dfs(i,j)
                    c+=1
        return c
