class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = 0
        for i in range(weeks):
            total += (7 * (2*i + 1 + 7)) // 2
        start = weeks + 1
        for i in range(days):
            total += start + i

        return total
