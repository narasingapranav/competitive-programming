# 🟠 intersection-of-two-linked-lists — Intersection of Two Linked Lists

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/intersection-of-two-linked-lists/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Accepted solution for Intersection of Two Linked Lists on LeetCode.

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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return NOne
        p1,p2=headA,headB
        while p1!=p2:
            p1=p1.next if p1 else headB
            p2=p2.next if p2 else headA
        return p1
```

</details>
