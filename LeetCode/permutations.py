from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=permutations(nums)
        a=[]
        for i in l:
            a.append(list(i))
        return a