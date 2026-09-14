# 🟠 longest-common-suffix-queries — Longest Common Suffix Queries

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-common-suffix-queries/) &nbsp;|&nbsp; **Solved:** 2026-05-28

---

## 📝 Summary

Accepted solution for Longest Common Suffix Queries on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class TrieNode:
    def __init__(self):
        self.chars = {}
        self.len_word = 0
        self.best = float("inf")
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, idx, word):
        curr = self.root
        for c in reversed(word):
            if c not in curr.chars:
                curr.chars[c] = TrieNode()
            curr = curr.chars[c]
            if curr.best == float("inf") or curr.len_word > len(word):
                curr.best = idx
                curr.len_word = len(word)
    def search(self, word):
        curr = self.root
        idx = -1
        for c in reversed(word):
            if c not in curr.chars:
                break
            curr = curr.chars[c]
            idx = curr.best
        return idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        min_len_idx = 0
        for i, word in enumerate(wordsContainer):
            trie.insert(i, word)
            if len(wordsContainer[min_len_idx]) > len(word):
                min_len_idx = i

        ans = []
        for word in wordsQuery:
            idx = trie.search(word)
            if idx == -1:
                ans.append(min_len_idx)
            else:
                ans.append(idx)

        return ans
```

</details>
