class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        l=set()
        for i in nums:
            if i<k:
                return -1
            l.add(i)
        return (len(l) - (1 if min(l)== k else 0))