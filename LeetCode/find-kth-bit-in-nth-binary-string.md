# 🟠 find-kth-bit-in-nth-binary-string — Find Kth Bit in Nth Binary String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Accepted solution for Find Kth Bit in Nth Binary String on LeetCode.

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
    def findKthBit(self, n: int, k: int) -> str:
        def create(n):
            if n==1:
                return '0'
            prev = create(n-1)
            inverted = ""
            for c in prev:
                inverted += "1" if c == "0" else "0" 
            return prev + "1" + inverted[::-1]
        s = create(n)
        return s[k-1]
```

</details>
