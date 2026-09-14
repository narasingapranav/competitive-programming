class Solution:
    def __init__(self):
        self.count=0
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        l=[]
        d=set()
        ad=set()
        co=set()
        def place(r,c):
            board[r][c]='Q'
        def remove(r,c):
            board[r][c]='.'
        def solve(r):
            if r==n:
                self.count+=1
                return
            for c in range(n):
                if c in co or (r-c) in d or (r+c) in ad:
                    continue
                place(r,c)
                co.add(c)
                d.add(r-c)
                ad.add(r+c)
                solve(r+1)
                remove(r,c)
                co.remove(c)
                d.remove(r-c)
                ad.remove(r+c)
        solve(0)
        return self.count
    def totalNQueens(self, n: int) -> int:
        return self.solveNQueens(n)
        