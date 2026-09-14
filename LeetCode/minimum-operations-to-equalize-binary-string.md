# 🟠 minimum-operations-to-equalize-binary-string — Minimum Operations to Equalize Binary String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/) &nbsp;|&nbsp; **Solved:** 2026-02-27

---

## 📝 Summary

Accepted solution for Minimum Operations to Equalize Binary String on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        zero = 0
        slen = len(s)

        for i in range(slen):
            zero += ~ord(s[i]) & 1

        if zero == 0:
            return 0

        if slen == k:
            return 1 if zero == slen else -1

        base = slen - k

        odd = max(math.ceil(zero / k), math.ceil((slen - zero) / base))

        odd += ~odd & 1

        even = max(math.ceil(zero / k), math.ceil(zero / base))

        even += even & 1

        res = float('inf')

        if (k & 1) == (zero & 1):
            res = min(res, odd)

        if (~zero & 1) == 1:
            res = min(res, even)

        return -1 if res == float('inf') else res
```

</details>
