class Solution {
    public int[] validSequence(String word1, String word2) {
        int n=word1.length();
        int m=word2.length();
        int[] last = new int[m];
        Arrays.fill(last,-1);
        int i=n-1;
        int j=m-1;
        while(i>=0 && j>=0){
            if (word1.charAt(i)==word2.charAt(j)){
                last[j--]=i;
            }
            i--;
        }
        int[] ans=new int[m];
        boolean canchange=true;
        i=0;
        j=0;
        while (i<n && j<m){
            if (word1.charAt(i)==word2.charAt(j)){
                ans[j++]=i;
            }
            else if(canchange && (j==m-1 || i<last[j+1])){
                ans[j++]=i;
                canchange=false;
            }
            if (j==m){
                return ans;
            }
            i++;
        }
        return new int[0];
    }
}