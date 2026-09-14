class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]<nums[h]:

                h=mid
            elif nums[mid]>nums[h]:
                l=mid+1          
            else:
                h-=1
        return nums[l]

'''

2,2,2,0,1

  2,2,0,1
   
    2,0,1

     0,1

     0




'''