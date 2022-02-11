import java.util.Arrays;

class Solution {
    // FASTER THAN 77% ON LEET CODE !!!!

    public static void main(String[] args) {
        System.out.println(checkInclusion("abca", "asdfabca"));
    }

    public static boolean checkInclusion(String s1, String s2) {
        int s1Length = s1.length();
        int s2Length = s2.length();
        if (s1Length > s2Length)
            return false;
        int[] s1Arr = new int[26];
        int[] s2Arr = new int[26];
        for (int i = 0; i < s1Length; i++) {
            s1Arr[s1.charAt(i) - 'a']++;
            s2Arr[s2.charAt(i) - 'a']++;
        }
        if (Arrays.equals(s1Arr, s2Arr))
            return true;
        for (int i = s1Length; i < s2Length; i++) {
            s2Arr[s2.charAt(i) - 'a']++;
            s2Arr[s2.charAt(i - s1Length) - 'a']--;
            if (Arrays.equals(s1Arr, s2Arr))
                return true;
        }
        return false;
    }
}