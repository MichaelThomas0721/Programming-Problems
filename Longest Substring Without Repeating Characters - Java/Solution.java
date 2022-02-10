import java.util.HashSet;

class Solution {
    // 5ms RUNTIME!!!!! FASTER THEN 87% ON LEETCODE!!!!!!!

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcadjiyhejold"));
    }

    public static int lengthOfLongestSubstring(String s) {
        int startPointer = 0;
        int maxCount = 0;
        HashSet<Character> letters = new HashSet();
        for (char letter : s.toCharArray()) {
            while (letters.contains(letter)) {
                letters.remove(s.charAt(startPointer));
                startPointer++;
            }
            letters.add(letter);
            if (letters.size() > maxCount) {
                maxCount = letters.size();
            }
        }
        return maxCount;
    }
}