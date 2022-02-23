import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    // Faster than 95.16% on Leetcode !!!
    public static void main(String[] args) {
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);

        node1.neighbors.add(node2);
        node1.neighbors.add(node4);

        node2.neighbors.add(node1);
        node2.neighbors.add(node3);

        node3.neighbors.add(node2);
        node3.neighbors.add(node4);

        node4.neighbors.add(node1);
        node4.neighbors.add(node3);

        Node newNode = cloneGraph(node1);
        System.out.println(newNode.val);
    }

    public static Node cloneGraph(Node node) {
        return (node == null) ? null : cloneGraph(node, new HashMap<>());
    }

    private static Node cloneGraph(Node node, HashMap<Integer, Node> map) {
        if (map.containsKey(node.val))
            return map.get(node.val);

        Node newNode = new Node(node.val);
        map.put(node.val, newNode);
        for (Node neighbor : node.neighbors) {
            newNode.neighbors.add(cloneGraph(neighbor, map));
        }
        return newNode;
    }
}

class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}