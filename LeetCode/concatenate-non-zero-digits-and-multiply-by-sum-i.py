class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0 : return 0
        s=""
        su=0
        for i in str(n):
            if i!="0":
                s+=i
                su+=int(i)
        s=int(s)
        return s*su
