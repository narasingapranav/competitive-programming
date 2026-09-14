class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=set()
        for i in nums:
            if i in c:
                return True
            c.add(i)
        return False