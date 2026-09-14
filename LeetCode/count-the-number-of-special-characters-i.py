class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for i in a:
            d[i] = i.upper()
        count = 0
        for i in a:
            if i in word and d[i] in word:
                count += 1
        return count