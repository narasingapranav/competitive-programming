class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def quick(arr):
            if len(arr)<=1:
                return arr
            p=arr[len(arr)//2]
            left=[i for i in arr if i<p]
            middle=[i for i in arr if i==p]
            right=[i for i in arr if i>p]
            return quick(left)+middle+quick(right)

        a=quick(nums)
        ind=[]
        for i in range(len(a)):
            if a[i]==target:
                ind.append(i)
        return ind