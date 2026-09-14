from math import isqrt


class Solution:
    def validSubarrays(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[bool]:
        n = len(nums)
        q = len(queries)
        block = isqrt(n) + 1
        qs = [(l, r, i) for i, (l, r) in enumerate(queries)]
        qs.sort(
            key=lambda x: (x[0] // block, x[1] if (x[0] // block) % 2 == 0 else -x[1])
        )
        values = {x: i for i, x in enumerate(set(nums))}
        arr = [values[x] for x in nums]
        freq = [0] * len(values)
        distinct = 0
        odd = 0
        ans = [False] * q
        L = 0
        R = -1

        def add(x):
            nonlocal distinct, odd
            if freq[x] == 0:
                distinct += 1
            if freq[x] % 2 == 1:
                odd -= 1
            freq[x] += 1
            if freq[x] % 2 == 1:
                odd += 1

        def remove(x):
            nonlocal distinct, odd
            if freq[x] % 2 == 1:
                odd -= 1
            freq[x] -= 1
            if freq[x] % 2 == 1:
                odd += 1
            if freq[x] == 0:
                distinct -= 1

        for l, r, idx in qs:
            while L > l:
                L -= 1
                add(arr[L])
            while R < r:
                R += 1
                add(arr[R])
            while L < l:
                remove(arr[L])
                L += 1
            while R > r:
                remove(arr[R])
                R -= 1
            ans[idx] = distinct == k and odd == 0
        return ans
