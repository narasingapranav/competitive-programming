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