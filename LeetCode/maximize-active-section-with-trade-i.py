class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        s='1'+s+'1'
        groups = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            groups.append((s[i], j - i))
            i = j
        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                left = groups[i - 1]
                right = groups[i + 1]
                if left[0] == '0' and right[0] == '0':
                    gain = left[1] + right[1]
        mx = 0
        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                if groups[i-1][0] == '0' and groups[i+1][0] == '0':
                    mx = max(mx, groups[i-1][1] + groups[i+1][1])
        return ones+mx