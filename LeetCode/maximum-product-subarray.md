# 🟠 maximum-product-subarray — Maximum Product Subarray

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Accepted solution for Maximum Product Subarray on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int maxProduct(int[] nums) {
        int l=1;
        int r=1;
        int ans=Integer.MIN_VALUE;
        int n=nums.length;
        for (int i=0;i<n;i++){
            if (l==0){
                l=nums[i];
            }
            else{
                l*=nums[i];
            }
            ans=Math.max(ans,l);
        }
        for (int i=n-1;i>=0;i--){
            if (r==0){
                r=nums[i];
            }
            else{
                r*=nums[i];
            }
            ans=Math.max(ans,r);
        }
        ans=Math.max(ans,r);
        ans=Math.max(ans,l);
        return ans;
    }
}
```

</details>
