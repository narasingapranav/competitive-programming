class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[0] - t[1])
        curr = 0
        ans  = 0
        for actual, minimum in tasks:
            if curr < minimum:
                ans  += (minimum - curr)
                curr  = minimum
            curr -= actual
        return ans