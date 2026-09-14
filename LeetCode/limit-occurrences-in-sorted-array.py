class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []

        for x in nums:
            n = len(ans)

            # Add element if it appears less than k times
            if n < k or ans[n - k] != x:
                ans.append(x)

        return ans