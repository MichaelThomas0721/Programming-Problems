import java.util.Stack;

class Solution {

    public static void main(String[] args) {
        System.out.println(removeKdigits("10", 1));
    }

    public static String removeKdigits(String num, int k) {
        int length = num.length();
        if (k == length)
            return "0";
        Stack<Character> stack = new Stack();
        int counter = 1;
        char last = num.charAt(0);
        char c = num.charAt(counter);
        while (counter < length) {
            while (last > c && k > 0) {
                k--;
                last = c;
                counter++;
                c = num.charAt(counter);
            }
            stack.push(num.charAt(counter - 1));
            last = num.charAt(counter);
            counter++;
            if (counter != length) {
                c = num.charAt(counter);
            }
        }
        if (stack.size() < length - k) {
            stack.push(num.charAt(length - 1));
        }

        StringBuilder sb = new StringBuilder();

        while (!stack.isEmpty()) {
            char current_char = stack.pop();
            sb.append(current_char);
        }
        sb.reverse();

        while (sb.length() > 1 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        return sb.toString();

        /*
         * while (counter < length) {
         * 
         * while (k > 0 && !stack.isEmpty() && stack.peek() > num.charAt(counter)) {
         * stack.pop();
         * k--;
         * }
         * stack.push(num.charAt(counter));
         * counter++;
         * }
         * 
         * while (k > 0) {
         * stack.pop();
         * k--;
         * }
         * 
         * StringBuilder sb = new StringBuilder();
         * 
         * while (!stack.isEmpty()) {
         * char current_char = stack.pop();
         * sb.append(current_char);
         * }
         * sb.reverse();
         * 
         * while (sb.length() > 1 && sb.charAt(0) == '0') {
         * sb.deleteCharAt(0);
         * }
         * return sb.toString();
         */
    }

}