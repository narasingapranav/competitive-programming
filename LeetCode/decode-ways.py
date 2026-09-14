class Solution:
    def numDecodings(self, s: str) -> int:
        prev, prevprev = 0, 0
        if s[0] == "0":
            return 0

        prev, prevprev = 1, 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != "0":
                curr = prev

            if s[i - 1] == "1" or (
                s[i - 1] == "2" and s[i] in ["0", "1", "2", "3", "4", "5", "6"]
            ):
                curr += prevprev

            prevprev = prev
            prev = curr

        return prev