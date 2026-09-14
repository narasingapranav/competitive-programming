# 🟠 customer-who-visited-but-did-not-make-any-transactions — Customer Who Visited but Did Not Make Any Transactions

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) &nbsp;|&nbsp; **Solved:** 2026-05-20

---

## 📝 Summary

Accepted solution for Customer Who Visited but Did Not Make Any Transactions on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select customer_id , count(visit_id) as count_no_trans from Visits where visit_id not in (select visit_id from Transactions ) group by customer_id
```

</details>
