class Solution:
    def isPalindromic(self, s: str) -> bool:
        res=''
        for i in s:
            res += format(ord(i), '08b')
        return res==res[::-1]