class Solution:
    def longestPalindrome(self, s: str) -> int:
        o=0
        a={}
        for i in s:
            a[i]=a.get(i,0)+1
            if a[i]%2==1:
                o+=1
            else:
                o-=1
        if o>0:
            return len(s)-o+1
        else:
            return len(s)