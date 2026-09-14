class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       k=nums
       k[::]=[i for i in k if i !=val]