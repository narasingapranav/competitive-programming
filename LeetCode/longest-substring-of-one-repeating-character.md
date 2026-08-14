# 🟠 longest-substring-of-one-repeating-character — Longest Substring of One Repeating Character

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Given a string s and a sequence of point updates, find the length of the longest substring consisting of a single repeating character after applying each update.

## 🔍 Key Observation

By storing the leftmost/rightmost characters along with the longest identical prefix, suffix, and overall maximum length at each Segment Tree node, two adjacent segments can be merged in O(1) time based on whether their boundary characters match.

## ⚙️ Algorithm

**Segment Tree**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O((n + q) log n)` | `O(n)` |

## 🏷️ Tags

`segment-tree` `string`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left
            lc, lrc, llen, lp, ls, lb = left
            rlc, rc, rlen, rp, rs, rb = right
            length = llen + rlen

            prefix = lp

            if lrc == rlc and lp == llen:
                prefix = llen + rp

            suffix = rs

            if lrc == rlc and rs == rlen:
                suffix = rlen + ls

            best = max(lb, rb)

            if lrc == rlc:
                best = max(best, ls + rp)

            return [lc, rc, length, prefix, suffix, best]

        def build(node, start, end):
            if start == end:
                tree[node] = [s[start], s[start], 1, 1, 1, 1]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, start, end, index, char):
            if start == end:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(tree[1][5])

        return answer
```

</details>
