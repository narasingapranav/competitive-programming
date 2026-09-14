class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def create(n):
            if n==1:
                return '0'
            prev = create(n-1)
            inverted = ""
            for c in prev:
                inverted += "1" if c == "0" else "0" 
            return prev + "1" + inverted[::-1]
        s = create(n)
        return s[k-1]