class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        answer = -1
        n = len(nums1)
        m = len(nums2)
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                answer = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return answer