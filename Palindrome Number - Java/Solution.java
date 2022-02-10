class Solution {
    // FASTER THAN 99.97% ON LEETCODE !!!!!

    public static void main(String[] args) {
        System.out.println(isPalindrome(0));
    }

    public static boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        if (x / 10 == 0)
            return true;
        if (x % 10 == 0)
            return false;
        int rev = 0;
        while (x > rev) {
            rev = rev * 10 + x % 10;
            x = x / 10;
        }
        if (rev == x || (x == rev / 10))
            return true;
        return false;
    }
}