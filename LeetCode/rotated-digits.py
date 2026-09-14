class Solution:
    def rotatedDigits(self, n: int) -> int:
        cnt=0
        for i in range(1,n+1):
            nu=str(i)
            if '3' in nu or '4' in nu or '7' in nu :
                continue
            if '2' in nu or '5' in nu or '6' in nu or '9' in nu:
                cnt+=1
        return cnt