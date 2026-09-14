class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        min_abs = float('inf')
        neg_count = 0
        for row in matrix:
            for num in row:
                if num < 0:
                    neg_count += 1
                total += abs(num)
                min_abs = min(min_abs, abs(num))
        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs