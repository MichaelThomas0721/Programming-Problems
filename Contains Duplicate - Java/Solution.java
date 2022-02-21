import java.util.HashMap;

class Solution {
    public static void main(String[] args) {
        // int[] nums = { 1, 2, 3, 1 };
        // int[] nums = { 1, 2, 3, 4 };
        int[] nums = { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 };
        System.out.println(containsDuplicate(nums));
    }

    public static boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap();
        for (int num : nums) {
            if (map.containsKey(num))
                return true;
            map.put(num, 1);
        }
        return false;

        // Slower solution
        /*
         * List<Integer> list = new ArrayList<>(Arrays.stream(nums).boxed().toList());
         * while (!list.isEmpty()) {
         * int temp = list.get(0);
         * list.remove(0);
         * if (list.contains(temp))
         * return true;
         * }
         * return false;
         */
    }
}