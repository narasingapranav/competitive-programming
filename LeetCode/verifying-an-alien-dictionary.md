# 🟠 verifying-an-alien-dictionary — Verifying an Alien Dictionary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/verifying-an-alien-dictionary/) &nbsp;|&nbsp; **Solved:** 2026-05-18

---

## 📝 Summary

Accepted solution for Verifying an Alien Dictionary on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i , char in enumerate(order)}

        for i in range (len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range (min(len(w1),len(w2))): 
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                       return False
                    break
            else:
               if len(w1) > len(w2):
                    return False


        return True     
```

</details>
