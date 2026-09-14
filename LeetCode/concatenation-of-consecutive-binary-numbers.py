class Solution:
    def convertbin(self,n):
        s=''
        while n>0:
            s+=str(n%2)
            n//=2
        return s[::-1]
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        arr = []
        for i in range(1, n + 1):
            arr.append(self.convertbin(i))
        a = ''.join(arr)
        return int(a, 2) % MOD