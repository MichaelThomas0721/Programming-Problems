class Solution {
    public static void main(String[] args) {
        ListNode l1 = new ListNode(3);
        ListNode l2 = new ListNode(1, l1);
        ListNode l3 = new ListNode(2, l2);
        ListNode l4 = new ListNode(4, l3);

        ListNode test = sortList(l4);
        while (test.next != null) {
            System.out.println(test.val);
            test = test.next;
            if (test.next == null) {
                System.out.println(test.val);
            }
        }
    }

    public static ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode middle, l1, l2;

        middle = findMiddle(head);
        l1 = head;
        l2 = middle.next;
        middle.next = null;

        l1 = sortList(l1);
        l2 = sortList(l2);
        return merge(l1, l2);

        /*
         * if (head == null)
         * return head;
         * ListNode current = head;
         * ListNode last = null;
         * while (current.next != null) {
         * if (current.val > current.next.val) {
         * if (last != null) {
         * last.next = current.next;
         * current.next = last.next.next;
         * last.next.next = current;
         * } else {
         * ListNode temp = current.next;
         * current.next = temp.next;
         * temp.next = current;
         * head = temp;
         * }
         * 
         * last = null;
         * current = head;
         * } else {
         * last = current;
         * current = current.next;
         * }
         * }
         * return head;
         */
    }

    public static ListNode merge(ListNode l1, ListNode l2) {
        ListNode preHead = new ListNode(0), cur = preHead;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }

        if (l1 == null) {
            cur.next = l2;
        } else {
            cur.next = l1;
        }
        return preHead.next;
    }

    public static ListNode findMiddle(ListNode head) {
        if (head == null)
            return head;
        ListNode slow = head, fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
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