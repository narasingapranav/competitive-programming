class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        res = []

        for n in nums:
            counts[n] += 1
        
        def helper(sub, counts):

            if len(sub) == len(nums):
                res.append(sub[::])
                return

            for n in counts:

                if counts[n] == 0:
                    continue
                
                counts[n] -= 1
                sub.append(n)

                helper(sub, counts)

                sub.pop()
                counts[n] += 1
        
        helper([], counts)
        return res
