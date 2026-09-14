class Solution:
    def removeZeros(self, n: int) -> int:
        a=str(n)
        x=''
        for i in a:
            if i !='0':
                x+=i
        return int(x)