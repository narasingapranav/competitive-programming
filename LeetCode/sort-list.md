# 🟠 sort-list — Sort List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sort-list/) &nbsp;|&nbsp; **Solved:** 2025-12-19

---

## 📝 Summary

Accepted solution for Sort List on LeetCode.

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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergesort(head):
            if not head or not head.next:
                return head
            l,r=split(head)
            l=mergesort(l)
            r=mergesort(r)
            return merge(l,r)
        def split(head):
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            mid=slow.next
            slow.next=None
            return head,mid
        def merge(l,r):
            dummy =tail=ListNode()
            while l and r:
                if l.val<r.val:
                    tail.next=l
                    l=l.next
                else:
                    tail.next=r
                    r=r.next
                tail=tail.next
            tail.next=l or r
            return dummy.next
        return mergesort(head)
```

</details>
