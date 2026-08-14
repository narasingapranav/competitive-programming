class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=[]
        for i in str(n):
            nums.append(int(i))
        n=len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])
        ans = int("".join(map(str, nums)))
        if ans > 2**31 - 1:
            return -1
        return ans