class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n <= 1:
            return 0
        stockPrices.sort()
        count = 1
        x1, y1 = stockPrices[0]
        x2, y2 = stockPrices[1]
        dx_prev = x2 - x1
        dy_prev = y2 - y1
        for i in range(2, n):
            x3, y3 = stockPrices[i]
            dx = x3 - x2
            dy = y3 - y2
            if dy * dx_prev != dy_prev * dx:
                count += 1
            dx_prev = dx
            dy_prev = dy
            x2, y2 = x3, y3
        return count