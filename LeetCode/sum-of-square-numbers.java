class Solution {
    public boolean judgeSquareSum(int c) {
        long l=0;
        long h=(int)Math.sqrt(c);
        while (l<=h){
            long ans=l*l + h*h;
            if (ans==c){
                return true;
            }
            else if (ans>c){
                h--;
            }
            else{
                l++;
            }
        }
        return false;
    }
}