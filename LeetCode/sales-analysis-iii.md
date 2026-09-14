# 🟠 sales-analysis-iii — Sales Analysis III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sales-analysis-iii/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Accepted solution for Sales Analysis III on LeetCode.

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
select distinct p.product_id,p.product_name 
from Product p join Sales s 
on p.product_id=s.product_id 
where p.product_id not in (
    select product_id 
    from Sales 
    where sale_date>'2019-03-31' or sale_date<'2019-01-01'
    )
```

</details>
