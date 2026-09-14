class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        def longest(arr):
            arr.sort()
            best = cur = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            return best
        h = longest(hBars)
        v = longest(vBars)
        side = min(h, v) + 1
        return side * side