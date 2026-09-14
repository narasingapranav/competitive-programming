class Solution:
    def dfs(self,grid,x,y):
        n,m=len(grid),len(grid[0])
        # check for out of bounds if yes 0
        if x<0 or x>=n or y<0 or y>=m or grid[x][y]==0: 
            return 0
        # store present value useful in BT
        curgold=grid[x][y]
        # take the present gold value and add to res
        grid[x][y]=0
        localmax=curgold
        dirs=[(1,0),(-1,0),(0,-1),(0,1)]
        # dfs
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            localmax=max(localmax,curgold+self.dfs(grid,nx,ny)) # find max of present and dfs
        # backtrack i.e, restore old value
        grid[x][y]=curgold
        return localmax
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # idea : traverse full matrix and perform dfs if not 0 return max gold
        maxg=0
        n,m=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    maxg=max(maxg,self.dfs(grid,i,j))
        return maxg
        