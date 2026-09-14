class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        sum_ = 0
        squaresum = 0
        while(n):
            rem = n%10
            sum_ += rem
            squaresum += (rem**2)
            n = n//10
        return squaresum - sum_ >= 50