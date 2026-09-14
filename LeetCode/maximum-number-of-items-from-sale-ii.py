from typing import List
from collections import defaultdict
import bisect


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        self.c = float('inf')

        n = len(items)

        freq = [0] * (n + 1)

        for f, p in items:
            self.c = min(self.c, p)
            freq[f] += 1

        mult = [0] * (n + 1)

        for f in range(1, n + 1):
            for v in range(f, n + 1, f):
                mult[f] += freq[v]

        mp = defaultdict(int)
        self.m = 0

        for f, p in items:
            d = mult[f] - 1

            if d <= 0:
                continue

            mp[p] += d
            self.m += d

        arr = sorted(mp.items())

        sz = len(arr)

        self.cost = [0] * sz
        self.cnt = [0] * sz
        self.pc = [0] * sz
        self.ps = [0] * sz

        cc = 0
        sc = 0

        for i, (price, count) in enumerate(arr):
            self.cost[i] = price
            self.cnt[i] = count

            cc += count
            sc += count * price

            self.pc[i] = cc
            self.ps[i] = sc

        self.tStar = 0

        for i in range(sz):
            if self.cost[i] < 2 * self.c:
                self.tStar = self.pc[i]
            else:
                break

        self.hMin = self.h(self.tStar)

        lo = 0
        hi = budget // self.c + self.m

        while lo < hi:
            mid = (lo + hi + 1) // 2

            if self.ok(mid, budget):
                lo = mid
            else:
                hi = mid - 1

        return lo

    def costOfFirst(self, t):
        if t <= 0:
            return 0

        idx = bisect.bisect_left(self.pc, t)

        if idx < len(self.pc) and self.pc[idx] == t:
            return self.ps[idx]

        prevCnt = 0 if idx == 0 else self.pc[idx - 1]
        prevCost = 0 if idx == 0 else self.ps[idx - 1]

        return prevCost + (t - prevCnt) * self.cost[idx]

    def h(self, t):
        return self.costOfFirst(t) - 2 * self.c * t

    def minHUpTo(self, u):
        if u < 0:
            return 10**30

        if u >= self.tStar:
            return self.hMin

        return self.h(u)

    def ok(self, k, budget):
        best = 10**30

        needBonus = (k + 1) // 2

        if needBonus <= self.m:
            best = min(best, self.costOfFirst(needBonus))

        u = min(self.m, (k - 1) // 2)

        mh = self.minHUpTo(u)

        if mh < 10**29:
            best = min(best, self.c * k + mh)

        return best <= budget