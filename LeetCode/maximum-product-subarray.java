class Solution {
    public int maxProduct(int[] nums) {
        int m=0;
        if (nums.length==1) return nums[0];
        for(int i=0;i<nums.length;i++){
            int p=1;
            for (int j=i;j<nums.length;j++){
                p*=nums[j];
                m=Math.max(p,m);
            }
        }
        return m;
    }
}