class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        l, w = max(
            dimensions,
            key=lambda x: (x[0] * x[0] + x[1] * x[1], x[0] * x[1])
        )
        return l * w