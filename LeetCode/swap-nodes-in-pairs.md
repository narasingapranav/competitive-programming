# 🟠 swap-nodes-in-pairs — Swap Nodes in Pairs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/) &nbsp;|&nbsp; **Solved:** 2025-12-06

---

## 📝 Summary

Accepted solution for Swap Nodes in Pairs on LeetCode.

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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        temp=dummy
        while temp.next and temp.next.next:
            f=temp.next
            s=temp.next.next

            f.next=s.next
            s.next=f
            temp.next=s
            temp=f
        return dummy.next


```

</details>
