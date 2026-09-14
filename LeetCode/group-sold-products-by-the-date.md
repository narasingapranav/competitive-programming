# 🟠 group-sold-products-by-the-date — Group Sold Products By The Date

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/group-sold-products-by-the-date/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for Group Sold Products By The Date on LeetCode.

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
select sell_date, count( DISTINCT product ) as num_sold , GROUP_CONCAT( DISTINCT product order by product ASC separator ',' ) as products FROM Activities GROUP BY sell_date order by sell_date ASC;
```

</details>
