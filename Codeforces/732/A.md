# 🔵 732A — Buy a Shovel

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/732/A) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Determine the minimum number of shovels, priced at k burles each, a person needs to buy so that the total cost can be paid using only 10-burle coins and at most one r-burle coin without receiving change.

## 🔍 Key Observation

The total cost for n shovels, n * k, must end in either a 0 or the digit r, and since the last digit repeats modulo 10, we only need to test values of n from 1 to 10.

## ⚙️ Algorithm

**Brute force / Loop search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`brute force` `math` `implementation`

<details>
<summary>💻 View solution</summary>

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();
        int r = sc.nextInt();

        for (int n = 1; n <= 10; n++) {
            int total = n * k;

            if (total % 10 == 0 || total % 10 == r) {
                System.out.println(n);
                break;
            }
        }
    }
}
```

</details>
