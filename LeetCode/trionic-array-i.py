class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        def is_strictly_increasing(arr: list[int], start: int, end: int) -> bool:
            for i in range(start + 1, end + 1):
                if arr[i] <= arr[i - 1]:
                    return False
            return True
        def is_strictly_decreasing(arr: list[int], start: int, end: int) -> bool:
            for i in range(start + 1, end + 1):
                if arr[i] >= arr[i - 1]:
                    return False
            return True
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                if (is_strictly_increasing(nums, 0, p) and
                        is_strictly_decreasing(nums, p, q) and
                        is_strictly_increasing(nums, q, n - 1)):
                    return True
        return False