class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(num):
            count=0
            for i in range(1,num+1):
                if num%i==0:
                    count+=1
            if count==2:
                return True
            return False
        c=0
        for i in range (left,right+1):
            b=bin(i)[2:]
            co=b.count('1')
            if isprime(co):
                c+=1
        return c