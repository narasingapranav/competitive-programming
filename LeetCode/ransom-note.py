from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc=Counter(ransomNote)
        mc=Counter(magazine)
        for i,j in rc.items():
            if mc[i]<j:
                return False
        return True