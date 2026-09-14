from typing import List
from bisect import bisect_left, insort

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2

        if idx <= mid:
            self.update(node * 2, start, mid, idx, val)
        else:
            self.update(node * 2 + 1, mid + 1, end, idx, val)

        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0

        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2

        return max(
            self.query(node * 2, start, mid, l, r),
            self.query(node * 2 + 1, mid + 1, end, l, r)
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        LIMIT = 50000

        obstacles = [0, LIMIT]

        seg = SegmentTree(LIMIT + 1)

        seg.update(1, 0, LIMIT, LIMIT, LIMIT)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                idx = bisect_left(obstacles, x)

                left = obstacles[idx - 1]
                right = obstacles[idx]

                insort(obstacles, x)

                seg.update(1, 0, LIMIT, x, x - left)
                seg.update(1, 0, LIMIT, right, right - x)

            else:
                x, sz = q[1], q[2]

                idx = bisect_left(obstacles, x)

                left = obstacles[idx - 1]

                best = seg.query(1, 0, LIMIT, 0, left)

                ans.append(max(best, x - left) >= sz)

        return ans