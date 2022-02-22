class Solution {

    // FASTER THAN 100.00% ON LEETCODE !!!
    public static void main(String[] args) {
        int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        // int[] nums = { 1 };
        // int[] nums = { 5, 4, -1, 7, 8 };
        System.out.println(maxSubArray(nums));
    }

    public static int maxSubArray(int[] nums) {
        int current = nums[0];
        int max = current;

        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            max = Math.max(current, max);
            // Same solution without the function
            /*
             * if (nums[i] > current + nums[i]) {
             * current = nums[i];
             * } else {
             * current += nums[i];
             * }
             * if (current > max)
             * max = current;
             */
        }
        return max;
    }
}