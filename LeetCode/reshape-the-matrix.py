class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened=[j for i in mat for j in i]
        res=[]
        if len(flattened) != r * c:
            return mat
        res = []
        for i in range(0, len(flattened), c):
            res.append(flattened[i : i + c])
        return res