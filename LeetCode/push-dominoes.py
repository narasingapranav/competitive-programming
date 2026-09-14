class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        f=[0]*n
        fo=0
        for i in range(n):
            if dominoes[i]=='L':
                fo=0
            elif dominoes[i]=='R':
                fo=n
            else:
                fo=max(fo-1,0)
            f[i]+=fo
        fo=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=='R':
                fo=0
            elif dominoes[i]=='L':
                fo=n
            else:
                fo=max(fo-1,0)
            f[i]-=fo
        res=[]
        for i in f:
            if i>0:
                res.append('R')
            elif i<0:
                res.append('L')
            else:
                res.append('.')
        return "".join(res)