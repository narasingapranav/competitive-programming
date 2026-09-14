# 🟠 market-analysis-i — Market Analysis I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/market-analysis-i/) &nbsp;|&nbsp; **Solved:** 2026-06-05

---

## 📝 Summary

Accepted solution for Market Analysis I on LeetCode.

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
select u.user_id as buyer_id,u.join_date,ifnull(count(o.order_id),0)as orders_in_2019 from Users u left join Orders o on u.user_id=o.buyer_id and year(order_date)='2019' group by u.user_id,u.join_date
```

</details>
