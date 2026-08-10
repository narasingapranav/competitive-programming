# 🟠 queue-reconstruction-by-height — Queue Reconstruction by Height

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Reconstruct a queue given each person's height and the count of people taller than or equal to them standing in front of them.

## 🔍 Key Observation

Sorting people by height in descending order (and by k in ascending order for ties) allows us to greedily insert each person into the output list at index k without invalidating the k-counts of taller people already placed.

## ⚙️ Algorithm

**Greedy + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`greedy` `sorting` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        res=[]
        for h,k in people:
            res.insert(k,(h,k))
        return res
```

</details>
