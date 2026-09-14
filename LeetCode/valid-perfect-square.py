class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r=int(math.sqrt(num))
        return r*r==num