class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(1, numRows):
            triangle.append([1] + [triangle[-1][i] + triangle[-1][i+1] for i in range(len(triangle[-1])-1)] + [1])
        return triangle