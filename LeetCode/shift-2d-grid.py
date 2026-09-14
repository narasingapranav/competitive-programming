
import numpy as np
class Solution:
    def shift(self,grid):
        m,n=len(grid),len(grid[0])
        grid=np.array(grid)
        grid=grid.flatten()
        grid = np.concatenate(([grid[-1]], grid[:-1]))
        grid=grid.reshape(m,n)
        return grid
                
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid=np.array(grid)
        while k>0:
            grid=self.shift(grid)
            k-=1
        return grid.tolist()