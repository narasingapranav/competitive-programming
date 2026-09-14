class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        if n==1 : return nums
        res=[]
        l,m=0,0
        for i in nums:
            if i<pivot:
                nums[l]=i
                l+=1
            elif i>pivot:
                res.append(i)
            else:
                m+=1
        return nums[:l]+[pivot]*m+res