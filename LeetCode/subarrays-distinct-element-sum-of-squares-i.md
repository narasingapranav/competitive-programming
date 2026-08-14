# 🟠 subarrays-distinct-element-sum-of-squares-i — Subarrays Distinct Element Sum of Squares I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Calculate the sum of the squared counts of distinct elements for all possible subarrays of an integer array.

## 🔍 Key Observation

When processing elements from left to right, adding the current element increases the distinct count by 1 for all subarrays starting between its previous occurrence plus one and the current index. A segment tree can efficiently update range values and track both linear sums and sum of squares.

## ⚙️ Algorithm

**Segment Tree with Lazy Propagation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`segment tree` `hash table` `array` `math`

<details>
<summary>💻 View solution</summary>

```python
class Node:
    def __init__(self, val):
        self.lb = 0
        self.hb = 0
        self.val = val
        self.sum = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self):
        self.tree = []

    def createtree(self, arr):
        n = len(arr)
        self.tree = [Node(0) for _ in range(4 * n)]
        self.createutility(arr, 0, n - 1, 0)

    def createutility(self, arr, lb, hb, pos):
        self.tree[pos].lb = lb
        self.tree[pos].hb = hb

        if lb == hb:
            self.tree[pos].val = arr[lb]
            self.tree[pos].sum = arr[lb]
            return

        mid = (lb + hb) // 2

        self.createutility(arr, lb, mid, 2 * pos + 1)
        self.createutility(arr, mid + 1, hb, 2 * pos + 2)

        self.tree[pos].val = (
            self.tree[2 * pos + 1].val +
            self.tree[2 * pos + 2].val
        )

        self.tree[pos].sum = (
            self.tree[2 * pos + 1].sum +
            self.tree[2 * pos + 2].sum
        )

    def update(self, lb, hb, val, pos=0):
        if hb < self.tree[pos].lb or lb > self.tree[pos].hb:
            return

        if lb <= self.tree[pos].lb and hb >= self.tree[pos].hb:
            n = self.tree[pos].hb - self.tree[pos].lb + 1

            old = self.tree[pos].val

            self.tree[pos].val += n * val
            self.tree[pos].sum += 2 * val * old + n * val * val
            self.tree[pos].lazy += val

            return

        self.push(pos)

        self.update(lb, hb, val, 2 * pos + 1)
        self.update(lb, hb, val, 2 * pos + 2)

        self.tree[pos].val = (
            self.tree[2 * pos + 1].val +
            self.tree[2 * pos + 2].val
        )

        self.tree[pos].sum = (
            self.tree[2 * pos + 1].sum +
            self.tree[2 * pos + 2].sum
        )

    def push(self, pos):
        if self.tree[pos].lazy != 0:
            val = self.tree[pos].lazy

            for child in [2 * pos + 1, 2 * pos + 2]:
                n = self.tree[child].hb - self.tree[child].lb + 1
                old = self.tree[child].val

                self.tree[child].val += n * val
                self.tree[child].sum += 2 * val * old + n * val * val
                self.tree[child].lazy += val

            self.tree[pos].lazy = 0

    def query(self, lb, hb, pos=0):
        if lb <= self.tree[pos].lb and hb >= self.tree[pos].hb:
            return self.tree[pos].sum

        if hb < self.tree[pos].lb or lb > self.tree[pos].hb:
            return 0

        self.push(pos)

        return (
            self.query(lb, hb, 2 * pos + 1) +
            self.query(lb, hb, 2 * pos + 2)
        )


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)

        st = SegmentTree()
        st.createtree([0] * n)

        last = {}
        ans = 0
        mod = 10**9 + 7

        for i in range(n):
            p = last.get(nums[i], -1)

            st.update(p + 1, i, 1)

            ans += st.query(0, i)
            ans %= mod

            last[nums[i]] = i

        return ans
```

</details>
