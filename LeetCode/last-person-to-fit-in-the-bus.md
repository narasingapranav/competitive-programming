# 🟠 last-person-to-fit-in-the-bus — Last Person to Fit in the Bus

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/) &nbsp;|&nbsp; **Solved:** 2026-05-25

---

## 📝 Summary

Accepted solution for Last Person to Fit in the Bus on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select person_name from (select person_name,turn,sum(weight) over (order by turn) as cum from queue) p1 where cum<=1000 order by turn desc limit 1
```

</details>
