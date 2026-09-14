class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        m = n + 1
        ans = ""
        for i in range(n):
            su = 0
            for j in range(i, n):
                su += int(s[j])
                if su == k:
                    sub = s[i:j+1]
                    if len(sub) < m or (len(sub) == m and sub < ans):
                        m = len(sub)
                        ans = sub
                    break
        return ans