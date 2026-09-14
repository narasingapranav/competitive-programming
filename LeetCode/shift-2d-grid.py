class Solution:
    def shift(self,grid):
        lastrow=[grid[i][-1] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])-1,0,-1):
                grid[i][j]=grid[i][j-1]
        for i in range(1,len(grid)):
            grid[i][0]=lastrow[i-1]
        grid[0][0]=lastrow[-1]
        return grid
                
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        while k>0:
            self.shift(grid)
            k-=1
        return grid