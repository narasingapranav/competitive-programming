# 🟠 jump-game-iii — Jump Game III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-iii/) &nbsp;|&nbsp; **Solved:** 2026-05-17

---

## 📝 Summary

Accepted solution for Jump Game III on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        vis = [False] * n
        vis[start] = True
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            forward = i + arr[i]
            backward = i - arr[i]
            if forward < n and not vis[forward]:
                vis[forward] = True
                q.append(forward)
            if backward >= 0 and not vis[backward]:
                vis[backward] = True
                q.append(backward)
        return False
```

</details>
