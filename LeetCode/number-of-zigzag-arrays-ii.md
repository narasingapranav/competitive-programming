# 🟠 number-of-zigzag-arrays-ii — Number of ZigZag Arrays II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-ii/) &nbsp;|&nbsp; **Solved:** 2026-06-24

---

## 📝 Summary

Accepted solution for Number of ZigZag Arrays II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^9) (estimated -- 9 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007

        m = r - l + 1
        sz = 2 * m

        def multiply(A, B):
            C = [[0] * sz for _ in range(sz)]

            for i in range(sz):
                for k in range(sz):
                    if A[i][k] == 0:
                        continue

                    cur = A[i][k]

                    for j in range(sz):
                        if B[k][j] == 0:
                            continue

                        C[i][j] = (C[i][j] + cur * B[k][j]) % MOD

            return C

        T = [[0] * sz for _ in range(sz)]

        for x in range(m):

            for y in range(x + 1, m):
                T[x][m + y] = 1

            for y in range(x):
                T[m + x][y] = 1

        result = [[0] * sz for _ in range(sz)]
        for i in range(sz):
            result[i][i] = 1

        power = n - 1

        while power:
            if power & 1:
                result = multiply(result, T)

            T = multiply(T, T)
            power >>= 1

        answer = 0

        for i in range(sz):
            row_sum = sum(result[i]) % MOD
            answer = (answer + row_sum) % MOD

        return answer
```

</details>
