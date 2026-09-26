class Solution {

    boolean check(String str,String s){
        int n = s.length();
        int m = str.length();
        int i = 0;
        int j = 0;
        while(i<m && j<n){
            if(str.charAt(i) == s.charAt(j)){
                i++;
                j++;
            }
           else j++;
        }
        return i == m;
    }
    public String findLongestWord(String s, List<String> d) {
        // code here
        Collections.sort(d,(a,b)->{
            if(a.length() != b.length()) return b.length()-a.length();
            return a.compareTo(b);
        });
        //String ans = "";
        for(String str:d){
            if(check(str,s)){
                return str;
            }
        }
    return "";
    }
}