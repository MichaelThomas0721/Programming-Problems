import java.util.TreeSet;

class Solution {

    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4 };
        System.out.println(minimumDeviation(nums));
    }

    public static int minimumDeviation(int[] nums) {
        TreeSet<Integer> list = new TreeSet<>();
        for (int num : nums) {
            if (num % 2 == 0) {
                list.add(num);
            } else {
                list.add(num * 2);
            }
        }

        if (list.size() == 1)
            return 0;

        int res = Integer.MAX_VALUE;

        while (!list.isEmpty()) {
            int min = list.first();
            int max = list.pollLast();
            res = Math.min(res, max - min);

            if (max % 2 != 0) {
                break;
            }
            list.add(max / 2);
        }
        return res;
    }
}