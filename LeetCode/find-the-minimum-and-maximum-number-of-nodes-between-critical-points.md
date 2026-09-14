# 🟠 find-the-minimum-and-maximum-number-of-nodes-between-critical-points — Find the Minimum and Maximum Number of Nodes Between Critical Points

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) &nbsp;|&nbsp; **Solved:** 2026-08-31

---

## 📝 Summary

Accepted solution for Find the Minimum and Maximum Number of Nodes Between Critical Points on LeetCode.

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        first = -1
        last = -1
        idx = 1
        min_dist = float('inf')

        prev = head
        curr = head.next

        while curr.next is not None:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = idx
                    last = idx
                else:
                    min_dist = min(min_dist, idx - last)
                    last = idx

            prev = curr
            curr = curr.next
            idx += 1

        if first == last:
            return [-1, -1]

        return [min_dist, last - first]
```

</details>
