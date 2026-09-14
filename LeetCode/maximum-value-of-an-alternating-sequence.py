class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        # s , s+m , s+m-1 , s+2m-1 , s+2m-2 , ......
        # max values are at 0,2,4,6 ....
        # so max val is at last even index n//2
        maxval=n//2
        return s+maxval*m-(maxval-1)