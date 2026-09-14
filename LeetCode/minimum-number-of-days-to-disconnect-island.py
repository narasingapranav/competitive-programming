class Solution:
    rowdir=[-1,0,1,0]
    coldir=[0,1,0,-1]
    def isvalidcell(self,r,c,rows,cols):
        return r>=0 and c>=0 and r<rows and c<cols
    def dfs(self,r,c,matrix,visited):
        visited[r][c]=True
        for d in range(4):
            newrow=r+self.rowdir[d]
            newcol=c+self.coldir[d]
            if self.isvalidcell(newrow,newcol,len(matrix),len(matrix[0])) and matrix[newrow][newcol]==1 and not visited[newrow][newcol] :
                self.dfs(newrow,newcol,matrix,visited)
    def countcomponent(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        islandcount=0
        visited=[[False]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==1 and not visited[r][c]:
                    islandcount+=1
                    self.dfs(r,c,matrix,visited)
        return islandcount
    def minDays(self,grid):
        if self.countcomponent(grid) !=1:
            return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    grid[r][c]=0
                    if self.countcomponent(grid) !=1:
                        return 1
                    grid[r][c]=1
        return 2