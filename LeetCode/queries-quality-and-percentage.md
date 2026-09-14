# 🟠 queries-quality-and-percentage — Queries Quality and Percentage

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/queries-quality-and-percentage/) &nbsp;|&nbsp; **Solved:** 2026-05-22

---

## 📝 Summary

Accepted solution for Queries Quality and Percentage on LeetCode.

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
select query_name,round(avg(cast(rating as decimal)/position),2) as quality,round(sum(case when rating<3 then 1 else 0 end) * 100 / count(*),2) as poor_query_percentage from queries group by query_name
```

</details>
