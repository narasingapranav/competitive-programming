class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set(nums1)
        mi=None
        for i in nums2:
            if i in s:
                if mi is None or i < mi:
                    mi=i
        return mi if mi is not None else -1