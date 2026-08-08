# 🟠 minimum-time-to-complete-trips — Minimum Time to Complete Trips

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-time-to-complete-trips/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Find the minimum total time required for a fleet of buses to complete at least a specified target number of trips.

## 🔍 Key Observation

The total number of completed trips in T units of time is monotonically non-decreasing with respect to T, enabling binary search over the answer range.

## ⚙️ Algorithm

**Binary search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log(min(time) * totalTrips))` | `O(1)` |

## 🏷️ Tags

`binary-search` `array`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        long l=1;
        long h=1l*Arrays.stream(time).min().getAsInt()*totalTrips;
        while(l<h){
            long m=l+(h-l)/2;
            long c=0;
            for(int x:time){
                c+=m/(long)x;
            }
            if (c>=totalTrips) h=m;
            else l=m+1;
        }
        return l;
    }
}
```

</details>
