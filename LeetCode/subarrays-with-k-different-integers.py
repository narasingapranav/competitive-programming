class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums, k):
        freq = defaultdict(int)
        left = 0
        count = 0
        distinct = 0

        for right in range(len(nums)):
            # include nums[right]
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            # shrink window if too many distinct
            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            # all subarrays ending at 'right'
            count += right - left + 1

        return count
