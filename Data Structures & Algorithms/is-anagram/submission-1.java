class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length())
            return false;

        HashMap<Character, Integer> slist = new HashMap<>();
        HashMap<Character, Integer> tlist = new HashMap<>();
        for(int i = 0; i < s.length(); i++)
        {
            slist.put(s.charAt(i), slist.getOrDefault(s.charAt(i), 0) + 1);
            tlist.put(t.charAt(i), tlist.getOrDefault(t.charAt(i), 0) + 1);
        }

        return slist.equals(tlist);
    }
}
