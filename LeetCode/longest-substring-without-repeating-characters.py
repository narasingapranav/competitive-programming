class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxlen=0
        se=set()
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen
            