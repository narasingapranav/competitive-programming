class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        left = 0
        for x in range(1, n + 1):
            left += x
            right = total - left + x 
            if left == right:
                return x
        return -1