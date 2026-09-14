# 🟠 find-users-with-high-token-usage — Find Users with High Token Usage

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-users-with-high-token-usage/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Accepted solution for Find Users with High Token Usage on LeetCode.

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
select user_id , count(user_id) as prompt_count , round((sum(tokens)/count(user_id)),2) as avg_tokens 
from prompts 
group by user_id 
having  count(prompt)>2 and max(tokens)>avg(tokens)
order by avg_tokens desc,user_id
```

</details>
