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