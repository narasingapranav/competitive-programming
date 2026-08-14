# 🟠 dota2-senate — Dota2 Senate

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/dota2-senate/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Predict which party will win the vote in the Dota2 Senate, given a string representing the initial party alignment of senators who act greedily in round-robin order to ban opposing senators.

## 🔍 Key Observation

Each active senator should greedily ban the earliest available senator of the opposing party to eliminate their turn as soon as possible.

## ⚙️ Algorithm

**Queue-based greedy simulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`queue` `greedy` `simulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=deque()
        d=deque()
        for i in range(len(senate)):
            if senate[i]=='R':
                r.append(i)
            else:
                d.append(i)
        n=len(senate)
        while r and d:
            if r[0]<d[0]:
                r.append(r.popleft()+n)
                d.popleft()
            else:
                d.append(d.popleft()+n)
                r.popleft()
        if r:
            return "Radiant"
        else:
            return "Dire"
```

</details>
