# 🟠 sum-of-distances — Sum of Distances

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-distances/) &nbsp;|&nbsp; **Solved:** 2026-04-23

---

## 📝 Summary

Accepted solution for Sum of Distances on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
from collections import defaultdict

class Solution:
    def distance(self, nums):
        mp = defaultdict(list)

        for i, val in enumerate(nums):
            mp[val].append(i)

        ans = [0] * len(nums)

        for idx in mp.values():
            k = len(idx)

            prefix = [0] * k
            prefix[0] = idx[0]

            for i in range(1, k):
                prefix[i] = prefix[i - 1] + idx[i]

            for i in range(k):
                left = i * idx[i] - (prefix[i - 1] if i > 0 else 0)
                right = (prefix[k - 1] - prefix[i]) - (k - i - 1) * idx[i]

                ans[idx[i]] = left + right

        return ans
```

</details>
