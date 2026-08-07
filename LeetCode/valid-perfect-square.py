class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        h=num
        while l<=h:
            mid=l+(h-l)//2
            if mid*mid==num:
                return True
            if mid*mid <num:
                l=mid+1
            else:
                h=mid-1
        return False