class Solution {
    public int[] evenOddBit(int n) {
        int e=0,o=0;
        int pos=0;
        while (n>0){
            if ((n&1)==1){
                if (pos%2==0) e++;
                else o++;   
            }
            n>>=1;
            pos++;
        }
        return new int[]{e,o};
    }
}