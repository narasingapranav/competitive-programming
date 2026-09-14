class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        l=[]
        def issafe(r,c,b):
            for i in range(n):
                for j in range(n):
                    if b[i][j]=='Q':
                        if abs(r-i)==abs(c-j) or r==i or c==j:
                            return False
            return True
        def place(r,c):
            board[r][c]='Q'
        def remove(r,c):
            board[r][c]='.'
        def solve(r):
            if r==n:
                l.append(["".join(r) for r in board])
            for c in range(n):
                if issafe(r,c,board):
                    place(r,c)
                    solve(r+1)
                    remove(r,c)
        solve(0)
        return l