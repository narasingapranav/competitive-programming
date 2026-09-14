# 🟠 game-of-life — Game of Life

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/game-of-life/) &nbsp;|&nbsp; **Solved:** 2026-08-24

---

## 📝 Summary

Accepted solution for Game of Life on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int findlive(int i,int j, int[][] board){
        int[][] dirs={{-1,0},{1,0},{0,1},{0,-1},{-1,-1},{-1,1},{1,-1},{1,1}};
        int livecount=0;
        int n=board.length;
        int m=board[0].length;
        for (int[] a:dirs){
            int ni=i+a[0];
            int nj=j+a[1];
            if (ni>=0 && ni<n && nj>=0 && nj<m){
                if(board[ni][nj]==1){
                    livecount++;
                }
            }
        }
        return livecount;
    }
    public void gameOfLife(int[][] board) {
        int[][] res= new int[board.length][board[0].length];
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j]==1 && (findlive(i,j,board)==2 ||findlive(i,j,board)==3) ){
                    res[i][j]=1;
                }
                else if (board[i][j]==0 && (findlive(i,j,board)==3)){
                    res[i][j]=1;
                }
                else{
                    res[i][j]=0;
                }
            }
        }
        for (int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                board[i][j]=res[i][j];
            }
        }
    }
}
```

</details>
