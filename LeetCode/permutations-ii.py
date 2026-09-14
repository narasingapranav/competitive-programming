class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l=permutations(nums)
        a=set()
        for i in l:
            a.add(tuple(i))
        b=[]
        for i in a:
            b.append(list(i))
        return b