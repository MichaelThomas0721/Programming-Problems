import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

    // FASTER THAN 71% ON LEET CODE !!!
    public static void main(String[] args) {
        // int[][] inteverals = { { 1, 4 }, { 3, 6 }, { 2, 8 } };
        // int[][] inteverals = { { 1, 4 }, { 2, 3 } };
        int[][] inteverals = { { 3, 10 }, { 4, 10 }, { 5, 11 } };
        System.out.println(removeCoveredIntervals(inteverals));
    }

    public static int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> (a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]));
        List<int[]> list = new ArrayList<>(Arrays.asList(intervals));
        int j;
        for (int i = 0; i < list.size(); i++) {
            if (i == list.size() - 1) {
                break;
            }
            if (list.get(i)[1] >= list.get(i + 1)[1]) {
                list.remove(i + 1);
                i--;
            }
        }
        return list.size();
    }
}
