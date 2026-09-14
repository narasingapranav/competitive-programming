# 🟠 remove-nth-node-from-end-of-list — Remove Nth Node From End of List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) &nbsp;|&nbsp; **Solved:** 2025-12-06

---

## 📝 Summary

Accepted solution for Remove Nth Node From End of List on LeetCode.

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=1
        dummy=ListNode(0,head)
        temp=dummy
        while temp.next:
            c+=1
            temp=temp.next
        pos=c-n-1
        x=1
        temp=dummy
        for i in range(pos):
            temp=temp.next
        temp.next=temp.next.next
        return dummy.next
```

</details>
