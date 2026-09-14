class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=1 and n not in s:
            s.add(n)
            sum=0
            while n>0:
                rem=n%10
                sum+=rem**2
                n//=10
            n=sum
        return n==1