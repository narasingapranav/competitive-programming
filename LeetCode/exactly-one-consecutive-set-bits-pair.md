# 🟠 exactly-one-consecutive-set-bits-pair — Exactly One Consecutive Set Bits Pair

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/) &nbsp;|&nbsp; **Solved:** 2026-06-06

---

## 📝 Summary

Accepted solution for Exactly One Consecutive Set Bits Pair on LeetCode.

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
    def consecutiveSetBits(self, n: int) -> bool:
        c=0
        while n>1:
            if (n&1) and ((n>>1)&1):
                c+=1
            n>>=1
        return c==1
```

</details>
