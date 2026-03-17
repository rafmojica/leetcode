class Solution {
    public boolean isAnagram(String s, String t) {
        // store each character of s in a hashmap
        // store each character of t in a hashmap
        // compare if both hashmaps contains the same values
        if (s.length() != t.length())
            return false;

        Map<Character, String> sHashMap = new HashMap<>();
        Map<Character, String> tHashMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sHashMap.put(s.charAt(i), sHashMap.get(s.charAt(i)) + 1);
            tHashMap.put(t.charAt(i), tHashMap.get(t.charAt(i)) + 1);
        }
        return sHashMap.equals(tHashMap);
    }
}