class Solution:
    def binaryGap(self, n: int) -> int:
        md=0
        cd=0
        flag=False
        while n>0:
            a=n%2
            if a==1:
                if flag:
                    md=max(md,cd)
                cd=1
                flag=True
            else:
                if flag:
                    cd+=1
            n//=2
        return md