class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        d={}
        for i in range(n):
            t=tuple(grid[i])
            d[t]=d.get(t,0)+1
        ans=0
        for j in range(n):
                col=tuple(grid[i][j] for i in range(n))
                if col in d:
                    ans+=d[col]
        return ans