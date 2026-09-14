class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0]* 101
        for x in nums:
            cnt[x] += 1
        for v in range(1,101):
            cnt[v] += cnt[v-1]
        return [0 if x == 0 else cnt[x-1] for x in nums]