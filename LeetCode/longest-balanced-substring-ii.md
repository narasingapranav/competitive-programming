# 🟠 longest-balanced-substring-ii — Longest Balanced Substring II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-balanced-substring-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-13

---

## 📝 Summary

Accepted solution for Longest Balanced Substring II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def mono(self, s: str) -> int:
        if not s:
            return 0
        cnt = 1
        ans = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans

    def duo(self, s: str, c1: str, c2: str) -> int:
        pos: Dict[int, int] = {0: -1}
        ans = 0
        delta = 0
        for i, ch in enumerate(s):
            if ch != c1 and ch != c2:
                pos.clear()
                pos[0] = i
                delta = 0
                continue

            if ch == c1:
                delta += 1
            else:
                delta -= 1

            if delta in pos:
                ans = max(ans, i - pos[delta])
            else:
                pos[delta] = i

        return ans

    def trio(self, s: str) -> int:
        cnt0 = cnt1 = cnt2 = 0  
        pos: Dict[Tuple[int, int], int] = {(0, 0): -1}
        ans = 0
        for i, ch in enumerate(s):
            if ch == 'a':
                cnt0 += 1
            elif ch == 'b':
                cnt1 += 1
            else:  
                cnt2 += 1

            key = (cnt1 - cnt0, cnt2 - cnt0)

            if key in pos:
                ans = max(ans, i - pos[key])
            else:
                pos[key] = i

        return ans

    def longestBalanced(self, s: str) -> int:
        return max(
            self.mono(s),
            self.duo(s, 'a', 'b'),
            self.duo(s, 'a', 'c'),
            self.duo(s, 'b', 'c'),
            self.trio(s),
        )
```

</details>
