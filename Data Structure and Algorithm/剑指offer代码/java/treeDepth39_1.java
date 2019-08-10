package jianzhiOffer;

public class treeDepth39_1 {
	
	public class TreeNode {
	    int val = 0;
	    TreeNode left = null;
	    TreeNode right = null;

	    public TreeNode(int val) {
	        this.val = val;

	    }
	}
	
    public int TreeDepth(TreeNode root) {
    	if(root == null) {
    		return 0;
    	}
    	int nLeft = TreeDepth(root.left);
    	int nRight = TreeDepth(root.right);
        if(nLeft > nRight) {
        	return nLeft + 1;
        }else {
        	return nRight + 1;
        }
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		               1
//		              / \
//		             2   3
//		            / \   \
//		           4   5   6
//		              /
//		              7
		treeDepth39_1 treeDepth = new treeDepth39_1();
		TreeNode root = treeDepth.new TreeNode(1);
		TreeNode root_2 = treeDepth.new TreeNode(2);
		TreeNode root_3 = treeDepth.new TreeNode(3);
		TreeNode root_4 = treeDepth.new TreeNode(4);
		TreeNode root_5 = treeDepth.new TreeNode(5);
		TreeNode root_6 = treeDepth.new TreeNode(6);
		TreeNode root_7 = treeDepth.new TreeNode(7);
		root.left = root_2;
		root.right = root_3;
		root_2.left = root_4;
		root_2.right = root_5;
		root_3.right = root_6;
		root_5.left = root_7;
		System.out.println(treeDepth.TreeDepth(root));		
	}

}
