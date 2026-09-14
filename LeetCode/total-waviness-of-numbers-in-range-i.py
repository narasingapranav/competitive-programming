class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2 + 1):
            s = str(num)
            if len(s) < 3:
                continue
            for i in range(1, len(s) - 1):
                left = int(s[i - 1])
                curr = int(s[i])
                right = int(s[i + 1])
                if (curr > left and curr > right) or (curr < left and curr < right):
                    total += 1
        return total