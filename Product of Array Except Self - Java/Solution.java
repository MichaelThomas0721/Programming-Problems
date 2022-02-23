class Solution {
    public static void main(String[] args) {
        // int[] nums = { 1, 2, 3, 4 };
        int[] nums = { -1, 1, 0, -3, 3 };
        System.out.println(productExceptSelf(nums));
    }

    public static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int num = 1;
        res[0] = 1;
        for (int i = 1; i < n; i++) {
            num = num * nums[i - 1];
            res[i] = num;
        }
        num = 1;
        for (int i = n - 2; i >= 0; i--) {
            num = num * nums[i + 1];
            res[i] *= num;
        }
        return res;

        // Slower solution that uses division
        /*
         * int product = 1;
         * int zeros = 0;
         * for (int num : nums) {
         * if (num != 0) {
         * product *= num;
         * } else {
         * zeros++;
         * }
         * }
         * for (int i = 0; i < nums.length; i++) {
         * if (zeros == 0) {
         * nums[i] = product / nums[i];
         * } else if (zeros > 1) {
         * nums[i] = 0;
         * } else if ((zeros == 1 && nums[i] == 0)) {
         * nums[i] = product;
         * } else {
         * nums[i] = 0;
         * }
         * System.out.println(nums[i]);
         * }
         * return nums;
         */
    }
}