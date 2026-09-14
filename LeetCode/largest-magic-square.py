class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # prefix sums
        prefixRow = [[0]*(n+1) for _ in range(m)]
        prefixCol = [[0]*(m+1) for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                prefixRow[i][j+1] = prefixRow[i][j] + grid[i][j]
                prefixCol[j][i+1] = prefixCol[j][i] + grid[i][j]
        
        def isMagic(i, j, k):
            # i,j is top left of kxk square
            # main diag and anti diag
            diag=0; anti=0
            for d in range(k):
                diag += grid[i+d][j+d]
                anti += grid[i+d][j+k-1-d]
            if diag != anti: 
                return False
            # check rows and columns
            for d in range(k):
                # row sum
                rsum = prefixRow[i+d][j+k] - prefixRow[i+d][j]
                # column sum
                csum = prefixCol[j+d][i+k] - prefixCol[j+d][i]
                if rsum != diag or csum != diag:
                    return False
            return True
        
        # try from max possible k down
        for k in range(min(m,n), 1, -1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if isMagic(i, j, k):
                        return k
        return 1