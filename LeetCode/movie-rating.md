# 🟠 movie-rating — Movie Rating

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/movie-rating/) &nbsp;|&nbsp; **Solved:** 2026-05-24

---

## 📝 Summary

Accepted solution for Movie Rating on LeetCode.

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
(Select u.name as results 
from MovieRating as m, Users as u 
where u.user_id = m.user_id Group By m.user_id 
Order by count(m.user_id) desc, u.name limit 1)
union all
(Select m.title as results
from MovieRating as r, Movies as m
where m.movie_id = r.movie_id 
and r.created_at like "2020-02-%"
Group By r.movie_id 
Order by avg(r.rating) desc, m.title limit 1);
```

</details>
