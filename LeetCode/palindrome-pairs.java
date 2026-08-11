class Solution {
    boolean pal(String st,int s,int e){
        while(s<e){
            if(st.charAt(s)!=st.charAt(e))return false;
            s++;e--;
        }
        return true;
    }
    public List<List<Integer>> palindromePairs(String[] words) {
        HashMap<String,Integer> hm=new HashMap<>();
        for(int i=0;i<words.length;i++){
            hm.put(new StringBuilder(words[i]).reverse().toString(),i);
        }
        List<List<Integer>> res=new ArrayList<List<Integer>>();
        Integer x=hm.get("");
        if(x!=null){
            for(int i=0;i<words.length;i++){
                if(i!=x && pal(words[i],0,words[i].length()-1)){
                  res.add(Arrays.asList(i,x));
                }
            }
        }
        for(int i=0;i<words.length;i++){
            int len=words[i].length();
            if(hm.containsKey(words[i])&&hm.get(words[i])!=i)res.add(Arrays.asList(i,hm.get(words[i])));
            for(int j=0;j<len;j++){
                if(j+1<len && pal(words[i],j+1,len-1)){
                    String s=words[i].substring(0,j+1);
                    if(hm.containsKey(s)){
                        res.add(Arrays.asList(i,hm.get(s)));
                    }
                }
                if(pal(words[i],0,j)){
                    String s=words[i].substring(j+1);
                    if(hm.containsKey(s)){
                        res.add(Arrays.asList(hm.get(s),i));
                    }
                }
            }
        }
        return res;
    }
}