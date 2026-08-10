class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,ArrayList<String>> d =new HashMap<>();
        List<List<String>> res= new ArrayList<>();
        for(String i:strs){
            char[] arr=i.toCharArray();
            Arrays.sort(arr);
            String b=new String(arr);
            if(!d.containsKey(b)){
                d.put(b,new ArrayList<>());
            }
            d.get(b).add(i);
        }
        res.addAll(d.values());
        return res;
    }
}