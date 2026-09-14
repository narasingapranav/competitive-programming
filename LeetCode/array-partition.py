class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a=[]
        for i in range(0,len(nums),2):
            a.append((nums[i],nums[i+1]))
        s=0
        for i in a:
            s+=min(i)
        return s