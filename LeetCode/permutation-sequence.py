class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        used = [0] * n 
        result = ""

        k -= 1

        for i in range(n):
            s = math.factorial(n-i-1)
            x = int(k / s) + 1
            k = k % s
            c = 0
            t = -1
            while c < x:
                t += 1
                if not used[t]:
                    c += 1
            used[t] = 1
            result += str(t + 1)

        return result