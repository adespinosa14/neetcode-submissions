class Solution {
    public boolean isAnagram(String s, String t) {

// If the length of the strings do not match, automatic fail
        if(s.length() != t.length())
            return false;

// Create the hashmaps

        Map<Character, Integer> s_map = new HashMap<>();
        Map<Character, Integer> t_map = new HashMap<>();

// Traverse through the string
        for(int i = 0; i < s.length(); i++)
        {
            
// Count how many of each character we have
            s_map.put(s.charAt(i), s_map.getOrDefault(s.charAt(i), 0) + 1);
            t_map.put(t.charAt(i), t_map.getOrDefault(t.charAt(i), 0) + 1);
        }

// Check if we have the same number of each character, and return it's boolean value
        return s_map.equals(t_map);
    }
}
