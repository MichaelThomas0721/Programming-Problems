class Solution {
    public static void main(String[] args) {
        System.out.println(titleToNumber("ZY"));
    }

    public static int titleToNumber(String columnTitle) {
        int ans = 0;
        for (int i = 0; i < columnTitle.length(); i++) {
            ans += (columnTitle.charAt(columnTitle.length() - i - 1) - 'A' + 1) * Math.pow(26, i);
        }
        return ans;
    }
}