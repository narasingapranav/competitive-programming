class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nei=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        def findlive(i,j):
            lc=0
            for di,dj in nei:
                ni,nj=i+di,j+dj
                if 0<=ni<len(board) and 0<=nj<len(board[0]):
                    if board[ni][nj]==1:
                        lc+=1
            return lc
        resbaord=[[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1 and findlive(i,j) in (2,3):
                    resbaord[i][j]=1
                elif board[i][j]==0 and findlive(i,j)==3:
                    resbaord[i][j]=1
                else:
                    resbaord[i][j]=0
        board[:]=resbaord 