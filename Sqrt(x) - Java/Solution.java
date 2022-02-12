class Solution {

    // Faster than 9% on Leet code :(

    public static void main(String[] args) {
        System.out.println("Output: " + mySqrt(2147395600));
    }

    public static int mySqrt(int x) {
        int count = 0;
        long value = 0;
        while (value <= x) {
            if (value == x) {
                return count;
            } else if (value < 0) {
                return count - 1;
            }
            count++;
            value = count * count;
        }
        count--;
        return count;
    }
}