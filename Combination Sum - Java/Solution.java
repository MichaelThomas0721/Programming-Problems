import java.util.ArrayList;
import java.util.List;

class Solution {

    // FASTER THAN 89.80% ON LEETCODE !!!

    public static void main(String[] args) {
        int[] candidates = { 2, 3, 6, 7 };
        System.out.println(combinationSum(candidates, 7));
    }

    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> combos = new ArrayList<>();
        findCombination(candidates, 0, target, new ArrayList<>(), combos);
        return combos;
    }

    public static void findCombination(int[] candidates, int index, int target, List<Integer> current,
            List<List<Integer>> combos) {
        if (target == 0) {
            combos.add(new ArrayList<>(current));
            return;
        }

        for (int i = index; i < candidates.length; i++) {
            if (candidates[i] <= target) {
                current.add(candidates[i]);
                findCombination(candidates, i, target - candidates[i], current, combos);
                current.remove((Integer) candidates[i]);
            }
        }
    }

}