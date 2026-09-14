# 🟠 reverse-nodes-in-k-group — Reverse Nodes in k-Group

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/) &nbsp;|&nbsp; **Solved:** 2026-07-04

---

## 📝 Summary

Accepted solution for Reverse Nodes in k-Group on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k<=1:
            return head
        def has_k_nodes(node):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while has_k_nodes(prev.next):
            curr = prev.next
            nxt = curr.next
            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr
        return dummy.next
```

</details>
