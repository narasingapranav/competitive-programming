# 🟠 course-schedule-ii — Course Schedule II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/course-schedule-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-27

---

## 📝 Summary

Accepted solution for Course Schedule II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = {}  
        stack = []

        def dfs(node):
            if node in visited:
                if visited[node] == 1:
                    return False  
                return True      

            visited[node] = 1 

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2 
            stack.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return stack[::-1]
```

</details>
