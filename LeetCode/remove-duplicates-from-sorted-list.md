# 🟠 remove-duplicates-from-sorted-list — Remove Duplicates from Sorted List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) &nbsp;|&nbsp; **Solved:** 2025-09-06

---

## 📝 Summary

Accepted solution for Remove Duplicates from Sorted List on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=set()
        current=head
        previous=None
        while current:
            if current.val in a:
                previous.next=current.next
            else:
                a.add(current.val)
                previous=current
            current=current.next
        return head
```

</details>
