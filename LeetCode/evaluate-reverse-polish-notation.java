class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> op =new Stack<>();  
        for(String s:tokens){
            if("+/-*".contains(s)){
                int b=op.pop();
                int a=op.pop();
                if(s.equals("+")) op.push(a+b);
                else if(s.equals("-")) op.push(a-b);
                else if(s.equals("/")) op.push(a/b);
                else if(s.equals("*")) op.push(a*b);
            }
            else{
                op.push(Integer.parseInt(s));
            }
        } 
        return(op.peek());
    }
}