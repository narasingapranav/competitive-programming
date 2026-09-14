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