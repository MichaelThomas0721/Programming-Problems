import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {

    public static void main(String[] args) {
        int[] nums = { 1, 0, 1 };
        System.out.println(singleNumber(nums));
    }

    public static int singleNumber(int[] nums) {
        ArrayList<Integer> numList = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (!numList.contains(nums[i])) {
                numList.add(nums[i]);
            } else {
                numList.remove((Integer) nums[i]);
            }
        }
        return numList.get(0);

        // Slower Solution
        /*
         * List<Integer> num1 = new ArrayList<Integer>();
         * for (int i = 0; i < num1.size();) {
         * int temp = num1.get(0);
         * num1.remove((Integer) temp);
         * if (!num1.contains(temp)) {
         * return temp;
         * }
         * num1.remove((Integer) temp);
         * }
         * return 0;
         */

    }
}