class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        sub=[grid[i][y:y+k] for i in range(x,x+k)]
        sub.reverse()
        for i in range(k):
            grid[x+i][y:y+k]=sub[i]
        return grid