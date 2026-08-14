# 🟠 reveal-cards-in-increasing-order — Reveal Cards In Increasing Order

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reveal-cards-in-increasing-order/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a deck of cards, reorder them so that following a specific reveal-and-move process reveals all cards in strictly increasing order.

## 🔍 Key Observation

Simulating the card-revealing process on a queue of original array indices allows us to place sorted card values into their correct positions.

## ⚙️ Algorithm

**Queue simulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`array` `queue` `sorting` `simulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq=deque()
        n=len(deck)
        for i in range(n):
            dq.append(i)
        res=[0]*n
        for i in range(n):
            x=dq.popleft()
            res[x]=deck[i]
            if dq :
                dq.append(dq.popleft())
        return res
```

</details>
