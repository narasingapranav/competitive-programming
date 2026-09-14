class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''z=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    z.append([i,j])
        n=len(matrix)
        m=len(matrix[0])
        for c in z:
            for i in range(n):
                for j in range(m):
                    if i==c[0] or j==c[1]:
                        matrix[i][j]=0'''
        c=set()
        r=set()
        n,m=len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(n):
            for j in range(m):
                if i in r or j in c:
                    matrix[i][j]=0