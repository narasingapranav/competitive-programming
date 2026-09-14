# 🟠 customers-who-bought-all-products — Customers Who Bought All Products

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/customers-who-bought-all-products/) &nbsp;|&nbsp; **Solved:** 2026-05-24

---

## 📝 Summary

Accepted solution for Customers Who Bought All Products on LeetCode.

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
select customer_id from Customer group by customer_id having count(distinct product_key)=(select count(product_key) from Product)
```

</details>
