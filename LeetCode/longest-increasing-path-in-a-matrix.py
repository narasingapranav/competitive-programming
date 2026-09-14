class Solution:
    def dfs(self,mat,i,j,table):
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        m,n=len(mat),len(mat[0])
        maxlen=1
        if table[i][j] != -1:
            return table[i][j]
        for dx,dy in dirs:
            nx,ny=i+dx,j+dy
            if nx>=0 and ny>=0 and nx<m and ny<n and mat[nx][ny]>mat[i][j]:
                maxlen=max(maxlen,1+self.dfs(mat,nx,ny,table))
        table[i][j]=maxlen
        return maxlen
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        longpl=0
        table = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                longpl=max(longpl,self.dfs(matrix,i,j,table))
        return longpl       