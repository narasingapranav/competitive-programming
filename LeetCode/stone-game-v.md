# 🟠 stone-game-v — Stone Game V

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game-v/) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Alice repeatedly splits an array of stone values into two contiguous parts, keeping the part with the smaller sum (or choosing either if equal) and adding its sum to her total score. The objective is to find the maximum score Alice can obtain.

## 🔍 Key Observation

Each state depends on a subsegment [l, r] and can be solved using interval dynamic programming; prefix sums enable O(1) segment sum queries while early-exit branch pruning optimizes transitions.

## ⚙️ Algorithm

**Dynamic Programming with Pruning**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^3)` | `O(n^2)` |

## 🏷️ Tags

`dynamic-programming` `memoization` `prefix-sum` `game-theory`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0
            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    # Alice keeps the left side.
                    #
                    # If ans >= 2 * left_sum, this split
                    # cannot improve the answer.
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(l, k)
                    )

                elif left_sum > right_sum:
                    # Alice keeps the right side.
                    #
                    # As k increases, right_sum decreases.
                    # If ans >= 2 * right_sum, then every
                    # later split is also useless.
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, r)
                    )

                else:
                    # Equal sums: Alice can choose either side.
                    ans = max(
                        ans,
                        left_sum + dfs(l, k),
                        right_sum + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)
```

</details>
