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