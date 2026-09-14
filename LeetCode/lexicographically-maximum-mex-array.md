# 🟠 lexicographically-maximum-mex-array — Lexicographically Maximum MEX Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/lexicographically-maximum-mex-array/) &nbsp;|&nbsp; **Solved:** 2026-05-31

---

## 📝 Summary

Accepted solution for Lexicographically Maximum MEX Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
