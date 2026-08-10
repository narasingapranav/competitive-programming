# 🟠 bulls-and-cows — Bulls and Cows

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/bulls-and-cows/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Compare a secret digit string with a guess digit string and return the number of 'bulls' (correct digit in correct position) and 'cows' (correct digit in wrong position).

## 🔍 Key Observation

Bulls are counted when characters at the same index match, while cows are calculated for unmatched positions by taking the sum of the minimum frequency of each digit present in both secret and guess.

## ⚙️ Algorithm

**Frequency counting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`string` `hash-table` `counting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        sc=[0]*10
        gc=[0]*10
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                sc[int(secret[i])]+=1
                gc[int(guess[i])]+=1
        cows=0
        for i in range(10):
            cows+=min(sc[i],gc[i])
        return str(bulls)+'A'+str(cows)+'B'
```

</details>
