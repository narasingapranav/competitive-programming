class Solution{
    public List<Integer> findSubstring(String s, String[] words){
        HashMap<String,Integer> hm= new HashMap<>();
        List<Integer> res= new ArrayList<>();
        for(String s1:words){
            hm.put(s1,hm.getOrDefault(s1,0)+1);
        }
        int len = words[0].length();
        int n = words.length;
        for (int offset = 0; offset < len; offset++) {
            int left = offset;
            int c = 0;
            HashMap<String,Integer> window = new HashMap<>();
            for (int j=offset; j+len<=s.length(); j+=len) {
                String x=s.substring(j,j+len);
                if(!hm.containsKey(x)){
                    window.clear();
                    c=0;
                    left=j+len;
                    continue;
                }
                c++;
                window.put(x,window.getOrDefault(x,0)+1);
                while(window.get(x)>hm.get(x)){
                    String y=s.substring(left,left+len);
                    int count=window.get(y);
                    window.put(y,count-1);
                    c--;
                    left+=len;
                }
                if(c==n){
                    res.add(left);
                    String y=s.substring(left,left+len);
                    int count=window.get(y);
                    window.put(y,count-1);
                    c--;
                    left+=len;
                }
            }
        }
        return res;
    }
}