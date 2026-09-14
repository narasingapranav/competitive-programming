class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a="abcdefghijklmnopqrstuvwxyz"
        s=set(word)
        count=0
        for i in a:
            if i in s and i.upper() in s:
                count+=1
        return count
