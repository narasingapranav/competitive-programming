# 🟠 magnetic-force-between-two-balls — Magnetic Force Between Two Balls

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/magnetic-force-between-two-balls/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Given an array of basket positions and $m$ balls, place all balls into baskets such that the minimum magnetic force (distance) between any two balls is maximized.

## 🔍 Key Observation

The check for whether it is possible to place $m$ balls with at least a target minimum distance between them is monotonic, allowing the use of binary search on the distance value combined with a greedy check.

## ⚙️ Algorithm

**Binary search + greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n + n log(max_pos - min_pos))` | `O(1)` |

## 🏷️ Tags

`binary-search` `greedy` `sorting` `array`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int l=1;
        int h=position[position.length-1]-position[0];
        while (l<=h){
            int mid=l+(h-l)/2;
            if(solve(mid,position,m)){
                l=mid+1;
            }
            else{
                h=mid-1;
            }
        }
        return h+1;
    }
    public boolean solve(int distance,int[] position,int m){
        int c=1;
        int last = position[0];
        for(int i=1;i<position.length;i++){
            if(position[i]-last >distance){
                c++;
                last = position[i];
                if(c==m){
                    return true;
                }
            }
        }
        return false;
    }
}
```

</details>
