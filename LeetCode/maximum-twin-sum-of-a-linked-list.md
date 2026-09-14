# 🟠 maximum-twin-sum-of-a-linked-list — Maximum Twin Sum of a Linked List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/) &nbsp;|&nbsp; **Solved:** 2026-06-14

---

## 📝 Summary

Accepted solution for Maximum Twin Sum of a Linked List on LeetCode.

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        half = []
        slow = fast = head

        while fast and fast.next:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        res = 0
        while slow:
            res = max(res, half.pop() + slow.val)
            slow = slow.next

        return res
```

</details>
