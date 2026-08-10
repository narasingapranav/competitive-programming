class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words= s.split(" ");
        if(pattern.length()!=words.length){
            return false;
        }
        HashMap<Character,String> c2w=new HashMap<>();
        HashMap<String,Character> w2c=new HashMap<>();
        for(int i=0;i<words.length;i++){
            if (c2w.containsKey(pattern.charAt(i)) && !c2w.get(pattern.charAt(i)).equals(words[i])){
                return false;
            }
            if (w2c.containsKey(words[i]) &&! w2c.get(words[i]).equals(pattern.charAt(i))){
                return false;
            }
            c2w.put(pattern.charAt(i),words[i]);
            w2c.put(words[i],pattern.charAt(i));
        }
        return true;
    }
}