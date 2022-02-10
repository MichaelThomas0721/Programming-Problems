class Solution {

    public static void main(String args[]) {
        // Test Data

        /*
         * ListNode l1 = new ListNode(3);
         * ListNode l2 = new ListNode(4, l1);
         * ListNode l3 = new ListNode(2, l2);
         * 
         * ListNode ll1 = new ListNode(4);
         * ListNode ll2 = new ListNode(6, ll1);
         * ListNode ll3 = new ListNode(5, ll2);
         */

        /*
         * ListNode l1 = new ListNode(9);
         * 
         * ListNode ll1 = new ListNode(9);
         * ListNode ll2 = new ListNode(9, ll1);
         * ListNode ll3 = new ListNode(9, ll2);
         * ListNode ll4 = new ListNode(9, ll3);
         * ListNode ll5 = new ListNode(9, ll4);
         * ListNode ll6 = new ListNode(9, ll5);
         * ListNode ll7 = new ListNode(9, ll6);
         * ListNode ll8 = new ListNode(9, ll7);
         * ListNode ll9 = new ListNode(9, ll8);
         * ListNode ll10 = new ListNode(1, ll9);
         */

        /*
         * ListNode l1 = new ListNode(4);
         * ListNode l2 = new ListNode(6, l1);
         * ListNode l3 = new ListNode(5, l2);
         * 
         * ListNode ll1 = new ListNode(1);
         * ListNode ll2 = new ListNode(0, ll1);
         * ListNode ll3 = new ListNode(0, ll2);
         * ListNode ll4 = new ListNode(0, ll3);
         * ListNode ll5 = new ListNode(0, ll4);
         * ListNode ll6 = new ListNode(0, ll5);
         * ListNode ll7 = new ListNode(0, ll6);
         * ListNode ll8 = new ListNode(0, ll7);
         * ListNode ll9 = new ListNode(0, ll8);
         * ListNode ll10 = new ListNode(1, ll9);
         * ListNode ll11 = new ListNode(0, ll10);
         * ListNode ll12 = new ListNode(0, ll11);
         * ListNode ll13 = new ListNode(0, ll12);
         * ListNode ll14 = new ListNode(0, ll13);
         * ListNode ll15 = new ListNode(0, ll14);
         * ListNode ll16 = new ListNode(0, ll15);
         * ListNode ll17 = new ListNode(0, ll16);
         * ListNode ll18 = new ListNode(0, ll17);
         * ListNode ll19 = new ListNode(0, ll18);
         * ListNode ll20 = new ListNode(1, ll19);
         * ListNode ll21 = new ListNode(0, ll20);
         * ListNode ll22 = new ListNode(0, ll21);
         * ListNode ll23 = new ListNode(0, ll22);
         * ListNode ll24 = new ListNode(0, ll23);
         * ListNode ll25 = new ListNode(0, ll24);
         * ListNode ll26 = new ListNode(0, ll25);
         * ListNode ll27 = new ListNode(0, ll26);
         * ListNode ll28 = new ListNode(0, ll27);
         * ListNode ll29 = new ListNode(0, ll28);
         * ListNode ll30 = new ListNode(0, ll29);
         * ListNode ll31 = new ListNode(1, ll30);
         */

        ListNode l1 = new ListNode(9);
        ListNode l2 = new ListNode(9, l1);
        ListNode l3 = new ListNode(9, l2);
        ListNode l4 = new ListNode(9, l3);

        ListNode ll1 = new ListNode(9);
        ListNode ll2 = new ListNode(9, ll1);
        ListNode ll3 = new ListNode(9, ll2);
        ListNode ll4 = new ListNode(9, ll3);
        ListNode ll5 = new ListNode(9, ll4);
        ListNode ll6 = new ListNode(9, ll5);
        ListNode ll7 = new ListNode(9, ll6);

        System.out.println(addTwoNumbers(ll6, l4));
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int num1 = 0;
        int carry = 0;
        ListNode firstNode = null;
        ListNode placeHolder = firstNode;
        while (l1 != null || l2 != null) {
            int l1Num = 0;
            int l2Num = 0;
            if (l1 != null) {
                l1Num = l1.val;
                if (l1.next == null) {
                    l1 = null;
                } else {
                    l1 = l1.next;
                }
            }
            if (l2 != null) {
                l2Num = l2.val;
                if (l2.next == null) {
                    l2 = null;
                } else {
                    l2 = l2.next;
                }
            }

            num1 = l1Num + l2Num + carry;
            int lastDigit = (num1 % 10);
            carry = (num1 / 10);

            if (firstNode == null) {
                firstNode = new ListNode(lastDigit);
                placeHolder = firstNode;
            } else {
                ListNode newNode = new ListNode(lastDigit);
                placeHolder.next = newNode;
                placeHolder = placeHolder.next;
            }

        }
        if (carry != 0) {
            ListNode newNode = new ListNode(carry);
            placeHolder.next = newNode;
            placeHolder = placeHolder.next;
        }
        return (firstNode);
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}