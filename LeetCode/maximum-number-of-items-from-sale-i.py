class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        bonus = [0] * n
        for i in range(n):
            f = items[i][0]
            cnt = 0
            for j in range(n):
                if items[j][0] % f == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + bonus[i])

        ans = 0

        for b in range(budget + 1):
            remaining = budget - b

            cheapest = min(x[1] for x in items)

            ans = max(ans, dp[b] + remaining // cheapest)

        return ans