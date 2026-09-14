# 🟠 weighted-word-mapping — Weighted Word Mapping

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/weighted-word-mapping/) &nbsp;|&nbsp; **Solved:** 2026-06-13

---

## 📝 Summary

Accepted solution for Weighted Word Mapping on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            remainder = total % 26
            ans.append(chr(ord('z') - remainder))

        return "".join(ans)
```

</details>
