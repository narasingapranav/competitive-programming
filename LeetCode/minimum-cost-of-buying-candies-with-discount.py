class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        l = len(cost)
        for i in range(0, l, 3):
            total += cost[i]
            if i + 1 < l:
                total += cost[i + 1]
        return total