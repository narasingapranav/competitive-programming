class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        def dfs(r,c):
            dirs=[[0,1],[0,-1],[1,0],[-1,0]]
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return
            if visited[r][c] or grid[r][c]=='0':
                return
            visited[r][c]=True
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                dfs(nr,nc)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and not visited[i][j]:
                    count+=1
                    dfs(i,j)
        return count