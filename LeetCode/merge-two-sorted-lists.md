# 🟠 merge-two-sorted-lists — Merge Two Sorted Lists

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) &nbsp;|&nbsp; **Solved:** 2025-09-06

---

## 📝 Summary

Accepted solution for Merge Two Sorted Lists on LeetCode.

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
class Solution:
    def mergeTwoLists(self, List1: Optional[ListNode], List2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        while List1 and List2:
            if List1.val < List2.val:
                tail.next=List1
                List1=List1.next
            else:
                tail.next=List2
                List2=List2.next
            tail=tail.next
        tail.next= List1 if List1 else List2
        return dummy.next
```

</details>
