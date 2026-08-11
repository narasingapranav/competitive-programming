class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int l=0;
        int h=tokens.length-1;
        int s=0;
        int m=0;
        while (l<=h){
            if(power>=tokens[l]){
                s++;
                power-=tokens[l];
                m=Math.max(m,s);
                l++;
            }
            else if(s>=1){
                s--;
                power+=tokens[h];
                h--;
            }
            else{
                break;
            }
        }
        return m;
    }
}