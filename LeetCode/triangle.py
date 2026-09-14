class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows = len(triangle)
        min_path_sum = [0] * (num_rows + 1)
        for row in range(num_rows - 1, -1, -1):
            for col in range(row + 1):
               min_path_sum[col] = min(min_path_sum[col], min_path_sum[col + 1]) + triangle[row][col]
        return min_path_sum[0]