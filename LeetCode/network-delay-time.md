# 🟠 network-delay-time — Network Delay Time

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/network-delay-time/) &nbsp;|&nbsp; **Solved:** 2026-08-17

---

## 📝 Summary

Find the minimum time required for a signal sent from a starting node k to reach every node in a directed weighted graph, or return -1 if any node is unreachable.

## 🔍 Key Observation

The total delay time is equivalent to the maximum of the shortest path distances from the source node k to all other nodes in the network.

## ⚙️ Algorithm

**Dijkstra's algorithm**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(E log V)` | `O(V + E)` |

## 🏷️ Tags

`graph` `shortest-path` `dijkstra` `heap`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int []>> adj =new ArrayList<>();
        for(int i=0;i<=n;i++){
            adj.add(new ArrayList<int []>());
        }
        for(int a[]:times){
            adj.get(a[0]).add(new int[]{a[1],a[2]});
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        int dist[]=new int[n+1];
        Arrays.fill(dist,1000000);
        dist[k]=0;
        pq.offer(new int[]{0,k});
        while(!pq.isEmpty()){
            int a[]=pq.poll();
            int d=a[0],u=a[1];
            if(d!=dist[u]){
                continue;
            }
            for(int b[]:adj.get(u)){
                int v=b[0],c=b[1];
                if(dist[v]>d+c){
                    dist[v]=d+c;
                    pq.add(new int[] {dist[v],v});
                }
            }
        }
        int mx=0;
        for(int i=1;i<=n;i++){
            mx=Math.max(mx,dist[i]);
        }
        return mx==1000000?-1:mx;
    }
}
```

</details>
