# 🟠 remove-duplicates-from-sorted-list-ii — Remove Duplicates from Sorted List II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-09

---

## 📝 Summary

Given the head of a sorted linked list, remove all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

## 🔍 Key Observation

Counting the frequency of each value in an initial pass allows us to easily filter out any node whose value appears more than once when building the output list.

## ⚙️ Algorithm

**Frequency Counting via Hash Map**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`linked-list` `hash-table` `dummy-node`

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
        dict={}
        cur=head
        while cur:
            dict[cur.val] = dict.get(cur.val, 0) + 1
            cur=cur.next
        dummy=ListNode(0)
        cur=dummy
        node=head
        while node:
            if dict[node.val]==1:
                cur.next=ListNode(node.val)
                cur=cur.next
            node=node.next
        return dummy.next
```

</details>
