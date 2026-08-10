# 🟠 bag-of-tokens — Bag of Tokens

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/bag-of-tokens/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Find the maximum score reachable by spending power on face-up tokens to gain score, or spending score on face-down tokens to regain power.

## 🔍 Key Observation

Greedily spend power on the smallest tokens to gain points at minimal cost, and sacrifice points on the largest tokens to gain the maximum power possible.

## ⚙️ Algorithm

**Two pointers + Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(1)` |

## 🏷️ Tags

`greedy` `two-pointers` `sorting` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r,s,m=0,len(tokens)-1,0,0
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                s+=1
                l+=1
                m=max(s,m)
            elif s>=1 and l<r:
                power+=tokens[r]
                s-=1
                r-=1
            else:
                break
        return m
```

</details>
