class Solution {

    public static void main(String args[]) {
        int[] nums = { 2, 7, 11, 15 };
        int[] answer = twoSum(nums, 9);
        System.out.println(answer[0] + ", " + answer[1]);
    }

    public static int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int a = 0; a < nums.length; a++) {
                if (nums[i] + nums[a] == target && i != a) {
                    return (new int[] { i, a });
                }
            }
        }
        return null;
    }
}