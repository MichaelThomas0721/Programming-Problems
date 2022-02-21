import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println(isAnagram(s, t));
    }

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        int[] letters_s = new int[26];
        int[] letters_t = new int[26];
        for (int i = 0; i < s.length(); i++) {
            letters_s[s.charAt(i) - 'a']++;
            letters_t[t.charAt(i) - 'a']++;
        }
        if (Arrays.equals(letters_s, letters_t))
            return true;
        return false;

        // Slower solution
        /*
         * HashMap<Character, Integer> map1 = new HashMap();
         * s.chars().mapToObj(c -> (char) c)
         * .forEach(c -> {
         * int count = map1.getOrDefault(c, 0) + 1;
         * map1.put(c, count);
         * });
         * HashMap<Character, Integer> map2 = new HashMap();
         * t.chars().mapToObj(c -> (char) c)
         * .forEach(c -> {
         * int count = map2.getOrDefault(c, 0) + 1;
         * map2.put(c, count);
         * });
         * if (map1.equals(map2))
         * return true;
         * return false;
         */
    }
}