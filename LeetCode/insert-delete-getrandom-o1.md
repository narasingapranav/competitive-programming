# 🟠 insert-delete-getrandom-o1 — Insert Delete GetRandom O(1)

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/) &nbsp;|&nbsp; **Solved:** 2026-09-07

---

## 📝 Summary

Design a data structure that supports inserting, deleting, and fetching a random element, with each operation executing in average O(1) time.

## 🔍 Key Observation

Combining a dynamic array with a hash map mapping values to their array indices allows O(1) random access, while deletion can be done in O(1) by swapping the target element with the last element in the array.

## ⚙️ Algorithm

**Hash Map + Dynamic Array (Swap with Last)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) average per operation` | `O(n)` |

## 🏷️ Tags

`hash-table` `array` `design` `randomized`

<details>
<summary>💻 View solution</summary>

```python
import random
class RandomizedSet:

    def __init__(self):
        self.l=[]

    def insert(self, val: int) -> bool:
        if val in self.l:
            return False
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.l:
            return False
        a=self.l.pop(self.l.index(val))
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

</details>
