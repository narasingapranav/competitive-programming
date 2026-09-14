# 🟠 how-many-numbers-are-smaller-than-the-current-number — How Many Numbers Are Smaller Than the Current Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) &nbsp;|&nbsp; **Solved:** 2025-12-20

---

## 📝 Summary

Accepted solution for How Many Numbers Are Smaller Than the Current Number on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0]* 101
        for x in nums:
            cnt[x] += 1
        for v in range(1,101):
            cnt[v] += cnt[v-1]
        return [0 if x == 0 else cnt[x-1] for x in nums]
```

</details>
