class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i.isalnum():
                st+=i.lower()
        low=0
        high=len(st)-1
        while low<=high:
            if st[low]!=st[high]:
                return False
            low+=1
            high-=1
        return True