import java.util.HashMap;

class Solution {

    public static void main(String[] args) {
        int[] nums = new int[] { 1, -1, 0 };
        System.out.println(subarraySum(nums, 0));
    }

    public static int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int sum = 0, count = 0;

        for (int n : nums) {
            sum += n;
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            int temp = 0;
            if (map.containsKey(sum))
                temp = map.get(sum);
            temp++;
            map.put(sum, temp);
        }
        return count;
    }
}