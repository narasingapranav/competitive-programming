# 🟠 actors-and-directors-who-cooperated-at-least-three-times — Actors and Directors Who Cooperated At Least Three Times

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/) &nbsp;|&nbsp; **Solved:** 2026-05-25

---

## 📝 Summary

Accepted solution for Actors and Directors Who Cooperated At Least Three Times on LeetCode.

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
select actor_id , director_id from ActorDirector group by actor_id,director_id having count(timestamp)>=3
```

</details>
