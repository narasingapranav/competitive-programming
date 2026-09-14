# 🟠 maximum-score-with-co-prime-element — Maximum Score with Co-Prime Element

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-score-with-co-prime-element/) &nbsp;|&nbsp; **Solved:** 2026-06-07

---

## 📝 Summary

Accepted solution for Maximum Score with Co-Prime Element on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion` `sorting`

<details>
<summary>💻 View solution</summary>

```python
def sieve(n):
    if n < 1: return []
    P = [1] * (n + 1)
    P[0], P[1] = 0, 0
    for i in range(int(sqrt(n)) + 1):
        if P[i] == 0: continue
        for j in range(i * i, n + 1, i): P[j] = 0
    return P


class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        # print(sorted(nums))
        n = len(nums)
        mx = max(max(nums), maxVal)
        P = sieve(mx + 1)
        P[1] = 1
        mp = Counter(nums)
        res = 0

        for i in range(mx + 1):
            if P[i]:
                if i in mp:
                    res = max(res, i - (mp[i] - 1))
                elif i <= maxVal:
                    res = max(res, i - 1)

        # print(res)
        for i in range(res, mx + 1):
            if i == 1:
                res = max(res, 1)
                continue
            t = 0
            if i in mp: t -= 1
            for j in range(n):
                if gcd(i, nums[j]) != 1: t += 1
                if i - t <= res: break
            else:
                if i not in mp: t = max(t, 1)

                if i > maxVal and i not in mp: continue

                a = i - t
                # print(i, t)
                res = max(res, a)

        return res
```

</details>
