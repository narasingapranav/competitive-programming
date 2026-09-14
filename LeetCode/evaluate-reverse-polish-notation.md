# 🟠 evaluate-reverse-polish-notation — Evaluate Reverse Polish Notation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) &nbsp;|&nbsp; **Solved:** 2025-12-13

---

## 📝 Summary

Accepted solution for Evaluate Reverse Polish Notation on LeetCode.

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

```java
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> op =new Stack<>();  
        for(String s:tokens){
            if("+/-*".contains(s)){
                int b=op.pop();
                int a=op.pop();
                if(s.equals("+")) op.push(a+b);
                else if(s.equals("-")) op.push(a-b);
                else if(s.equals("/")) op.push(a/b);
                else if(s.equals("*")) op.push(a*b);
            }
            else{
                op.push(Integer.parseInt(s));
            }
        } 
        return(op.peek());
    }
}
```

</details>
