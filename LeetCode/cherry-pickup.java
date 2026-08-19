class Solution {
    public int cherryPickup(int[][] grid) {
        int n=grid.length;int m=2*n-1;
        int dp[][]=new int[n][n];
        dp[0][0]=grid[0][0];
        for(int k=1;k<m;k++){
            for(int i=n-1;i>=0;i--){
                for(int j=n-1;j>=0;j--){
                    int p=k-i,q=k-j;
                    if(p<0||p>=n||q<0||q>=n||grid[i][p]<0||grid[j][q]<0){
                        dp[i][j]=-1;continue;
                    }
                    if(i>0)dp[i][j]=Math.max(dp[i][j],dp[i-1][j]);
                    if(j>0)dp[i][j]=Math.max(dp[i][j],dp[i][j-1]);
                    if(i>0&&j>0)dp[i][j]=Math.max(dp[i][j],dp[i-1][j-1]);
                    if(dp[i][j]>=0)dp[i][j]+=grid[i][p]+((i!=j)?grid[j][q]:0);
                   
                }
            }
        }
        return dp[n-1][n-1]>=0?dp[n-1][n-1]:0;
    }
}