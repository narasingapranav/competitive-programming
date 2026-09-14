class Solution:
    def countingSort(self, nums, exp):
        n = len(nums)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (nums[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            output[count[index] - 1] = nums[i]
            count[index] -= 1
        for i in range(n):
            nums[i] = output[i]
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        neg = [-x for x in nums if x < 0]
        pos = [x for x in nums if x >= 0]

        if neg:
            max_neg = max(neg)
            exp = 1
            while max_neg // exp > 0:
                self.countingSort(neg, exp)
                exp *= 10

        if pos:
            max_pos = max(pos)
            exp = 1
            while max_pos // exp > 0:
                self.countingSort(pos, exp)
                exp *= 10

        neg = [-x for x in reversed(neg)]
        return neg + pos
