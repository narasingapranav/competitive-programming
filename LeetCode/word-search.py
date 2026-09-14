'''
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis=[[False]*(len(board[0])+ 1) for _ in range(len(board) + 1)]
        def dfs(r,c,ind):
            if ind==len(word):
                return True
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c] !=word[ind] or vis[r][c] :
                return False
            vis[r][c]=True
            dirs=[[1,0],[0,1],[-1,0],[0,-1]]
            for i,j in dirs:
                nx,ny=r+i,c+j
                if dfs(nx,ny,ind+1):
                    return True
            vis[r][c]=False
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False