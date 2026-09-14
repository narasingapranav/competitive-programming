class Solution {
    public int missingMultiple(int[] nums, int k) {
        HashSet<Integer> s= new HashSet<>();
        for (int i:nums){
            s.add(i);
        }
        int m=Arrays.stream(nums).max().getAsInt();;
        for(int i=k;i<=m+k;i+=k){
            if (!s.contains(i)){
                return i;
            }
        }
        return 0;
    }
}