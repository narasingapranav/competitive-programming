from typing import List
from collections import Counter

class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []
        i = 0
        n = len(nums)

        while i < n:
            mex = 0
            while cnt[mex] > 0:
                mex += 1

            # If mex = 0, take one element at a time
            if mex == 0:
                res.append(0)
                cnt[nums[i]] -= 1
                i += 1
                continue

            seen = set()
            need = mex

            j = i
            while j < n:
                x = nums[j]
                cnt[x] -= 1

                if x < mex and x not in seen:
                    seen.add(x)
                    need -= 1

                j += 1
                if need == 0:
                    break

            res.append(mex)
            i = j

        return res