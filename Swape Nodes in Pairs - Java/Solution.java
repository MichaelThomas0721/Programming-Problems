class Solution {

    public static void main(String[] args) {

        // FASTER THAN 100.00% ON LEET CODE !!!!
        ListNode l1 = new ListNode(4);
        ListNode l2 = new ListNode(3, l1);
        ListNode l3 = new ListNode(2, l2);
        ListNode l4 = new ListNode(1, l3);

        ListNode outNode = swapPairs(l4);

        while (outNode != null) {
            System.out.println(outNode.val);
            outNode = outNode.next;
        }
    }

    public static ListNode swapPairs(ListNode head) {
        ListNode current = head;
        ListNode temp = null;
        ListNode nextTemp = null;
        while (current != null) {
            if (temp != null) {
                temp.next = current.next;
                current.next = temp;
                if (nextTemp != null) {
                    nextTemp.next = current;
                } else {
                    head = current;
                }
                nextTemp = temp;
                temp = null;
                current = current.next;
            } else {
                temp = current;
            }
            current = current.next;
        }
        return head;
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