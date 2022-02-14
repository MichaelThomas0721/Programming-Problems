import java.util.ArrayList;

class Solution {
    // RUNTIME FASTER THAN 100% ON LEET CODE !!! RAN IN 0MS !!!

    public static void main(String[] args) {
        TreeNode tn1 = new TreeNode(7);
        TreeNode tn2 = new TreeNode(15);
        TreeNode tn3 = new TreeNode(20, tn2, tn1);
        TreeNode tn4 = new TreeNode(9);
        TreeNode tn5 = new TreeNode(3, tn4, tn3);
        System.out.println(maxDepth(tn5));
    }

    public static int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        return (1 + Math.max(maxDepth(root.left), maxDepth(root.right)));
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}