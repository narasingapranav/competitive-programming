# 🟠 minimum-jumps-to-reach-end-via-prime-teleportation — Minimum Jumps to Reach End via Prime Teleportation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/) &nbsp;|&nbsp; **Solved:** 2026-05-08

---

## 📝 Summary

Accepted solution for Minimum Jumps to Reach End via Prime Teleportation on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`graph` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        mx = max(nums)
        spf = list(range(mx + 1))
        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        mp = {}
        for i, val in enumerate(nums):
            x = val
            used = set()
            while x > 1:
                p = spf[x]
                if p not in used:
                    if p not in mp:
                        mp[p] = []
                    mp[p].append(i)
                    used.add(p)
                x //= p
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        while q:
            i = q.popleft()
            steps = dist[i]
            if i == n - 1:
                return steps
            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = steps + 1
                q.append(i - 1)
            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = steps + 1
                q.append(i + 1)
            val = nums[i]
            if val > 1 and spf[val] == val:
                for nxt in mp.get(val, []):
                    if dist[nxt] == -1:
                        dist[nxt] = steps + 1
                        q.append(nxt)
                mp[val] = []
        return -1
```

</details>
