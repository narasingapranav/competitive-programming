# 🟠 merge-two-sorted-lists — Merge Two Sorted Lists

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) &nbsp;|&nbsp; **Solved:** 2026-07-02

---

## 📝 Summary

Accepted solution for Merge Two Sorted Lists on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* head1, struct ListNode* head2) {
    if (head1==NULL){
        return head2;
    }
    if (head2==NULL){
        return head1;
    }
    if (head1->val<head2->val){
        head1->next=mergeTwoLists(head1->next,head2);
        return head1;
    }
    else{
        head2->next=mergeTwoLists(head1,head2->next);
        return head2;
    }
}
```

</details>
