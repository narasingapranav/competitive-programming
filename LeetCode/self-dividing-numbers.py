class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        def solu(n):
            d=n
            while(n):
                
                r=n%10
                if r==0:
                    return False
                if d%r!=0:
                    return False
                n=n//10
            return True

        for i in range(left,right+1):
            x=solu(i)
            if x:
                ans.append(i)
        return ans