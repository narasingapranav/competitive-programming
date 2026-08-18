class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j,ids):
            if i<0 or j<0 or j>=len(grid[0]) or i>=len(grid) or grid[i][j]!=1:
                return 0   
            grid[i][j]=ids
            return 1+dfs(grid,i,j-1,ids)+dfs(grid,i,j+1,ids)+dfs(grid,i+1,j,ids)+dfs(grid,i-1,j,ids)
        n=len(grid)
        ids=2
        c=0
        res=0
        count=[0]*(n*n+3)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    ids += 1
                    count[ids] = dfs(grid, i, j, ids)
                    res = max(res, count[ids])
                else:
                    c+=1
        if c==0:
            return res
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    c=1
                    seen=set()
                    dirs=[(0,1),(1,0),(-1,0),(0,-1)]
                    for di,dj in dirs:
                        ni=i+di
                        nj=j+dj
                        if n>ni>=0 and n>nj>=0 and grid[ni][nj]!=0:
                            if grid[ni][nj] not in seen:
                                seen.add(grid[ni][nj])
                                c+=count[grid[ni][nj]]
                    res=max(res,c)
        return res