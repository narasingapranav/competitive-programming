# 🟠 hand-of-straights — Hand of Straights

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/hand-of-straights/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Determine if a hand of cards can be divided into groups of size `groupSize` such that each group contains consecutive integers.

## 🔍 Key Observation

To form valid consecutive groups, always start a group with the smallest available card value that has a remaining non-zero frequency.

## ⚙️ Algorithm

**Greedy + Hash Map + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N log N)` | `O(N)` |

## 🏷️ Tags

`greedy` `hash-table` `sorting` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        d={}
        for i in hand:
            d[i]=d.get(i,0)+1
        for i in sorted(hand):
            if d[i]==0:
                continue
            for j in range(i,i+groupSize):
                if d.get(j,0)==0:
                    return False
                d[j]-=1
        return True 
```

</details>
