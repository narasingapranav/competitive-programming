# 🟠 merge-k-sorted-lists — Merge k Sorted Lists

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) &nbsp;|&nbsp; **Solved:** 2026-07-07

---

## 📝 Summary

Accepted solution for Merge k Sorted Lists on LeetCode.

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
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        dummy = ListNode()
        temp=dummy
        
        while heap:
            val,i,node=heapq.heappop(heap)
            temp.next=node
            temp=temp.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return dummy.next        
```

</details>
