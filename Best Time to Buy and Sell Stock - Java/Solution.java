class Solution {
    public static void main(String[] args) {
        int[] prices = { 7, 1, 5, 3, 6, 4 };
        System.out.println(maxProfit(prices));
    }

    public static int maxProfit(int[] prices) {
        int profit = 0;
        int min = Integer.MAX_VALUE;
        for (int price : prices) {
            // Same thing without using the functions
            /*
             * if (price < min) {
             * min = price;
             * }
             * if (profit < price - min) {
             * profit = price - min;
             * }
             */
            min = Math.min(price, min);
            profit = Math.max(profit, price - min);
        }
        return profit;
    }
}