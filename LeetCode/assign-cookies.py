class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # sort based upon gree factor
        s.sort() 
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i