import java.util.Stack;

class Solution {

    // Faster than 99.39& on Leetcode !!!
    public static void main(String[] args) {
        System.out.println(isValid("{[]}["));
    }

    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack();

        for (char c : s.toCharArray()) {
            switch (c) {
                case '{', '(', '[':
                    stack.push(c);
                    break;
                case '}', ')', ']':
                    if (!stack.isEmpty() && stack.peek() == reverseParentheses(c)) {
                        stack.pop();
                        break;
                    } else
                        return false;
            }
        }
        return stack.isEmpty();
    }

    public static char reverseParentheses(char c) {
        switch (c) {
            case '}':
                return '{';
            case ']':
                return '[';
            case ')':
                return '(';
        }
        return '{';
    }
}