class Solution:
    def rotatedDigits(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            isrot = False
            valid = True
            for j in str(i):
                if j in "347":
                    valid = False
                    break
                if j in "2569":
                    isrot = True
            if valid and isrot:
                cnt += 1
        return cnt