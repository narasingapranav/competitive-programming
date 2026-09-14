class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total_area = 0
        low = float('inf')
        high = float('-inf')
        for x, y, l in squares:
            total_area += l * l
            low = min(low, y)
            high = max(high, y + l)
        half = total_area / 2
        def area_below(Y):
            area = 0
            for x, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    area += l * l
                else:
                    area += (Y - y) * l
            return area
        for _ in range(60):  
            mid = (low + high) / 2
            if area_below(mid) < half:
                low = mid
            else:
                high = mid
        return low