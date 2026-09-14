class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        a=nums1[0]
        flag=False
        for i in nums1:
            if i<a:
                a=i
            if i&1:
                flag=True
        if a&1:
            return True
        return not flag