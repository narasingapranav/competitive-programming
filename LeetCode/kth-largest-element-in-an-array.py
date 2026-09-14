import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q=[]
        for i in nums:
            heapq.heappush(q,-i)
        for i in range(k-1):
            heapq.heappop(q)
        return -1*heapq.heappop(q)