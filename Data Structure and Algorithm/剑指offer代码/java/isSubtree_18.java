package jianzhiOffer;

public class isSubtree_18 {
	
	class TreeNode {
	    int val = 0;
	    TreeNode left = null;
	    TreeNode right = null;

	    public TreeNode(int val) {
	        this.val = val;
	    }
	}
	
	public boolean HasSubtree(TreeNode root1, TreeNode root2) {
		boolean result = false;
		
		if(root1 != null && root2 != null) {
			if(root1.val == root2.val) {
				result = DoesTree1HaveTree2(root1,root2);
			}
			if(result == false) {
				result = HasSubtree(root1.left, root2);
			}
			if(result == false) {
				result = HasSubtree(root1.right, root2);
			}
		}
		return result;
	}
	
	public boolean DoesTree1HaveTree2(TreeNode root1, TreeNode root2) {
		if(root2 == null)
			return true;
		if(root1 == null)
			return false;
		if(root1.val != root2.val)
			return false;
		
		return DoesTree1HaveTree2(root1.left, root2.left) && DoesTree1HaveTree2(root1.right, root2.right);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		isSubtree_18 subtree = new isSubtree_18();
		//创建A树
//		              8
//		             / \
//		            8   7
//		           / \
//		          9   2
//		             / \
//		            4   7
		TreeNode root1_1 = subtree.new TreeNode(8);
		TreeNode root1_2 = subtree.new TreeNode(8);
		TreeNode root1_3 = subtree.new TreeNode(7);
		TreeNode root1_4 = subtree.new TreeNode(9);
		TreeNode root1_5 = subtree.new TreeNode(2);
		TreeNode root1_6 = subtree.new TreeNode(4);
		TreeNode root1_7 = subtree.new TreeNode(7);
		root1_1.left = root1_2;
		root1_1.right = root1_3;
		root1_2.left = root1_4;
		root1_2.right = root1_5;
		root1_5.left = root1_6;
		root1_5.right = root1_7;
		//创建B树
//		              8
//		             / \
//		            9   2
		TreeNode root2_1 = subtree.new TreeNode(8);
		TreeNode root2_2 = subtree.new TreeNode(9);
		TreeNode root2_3 = subtree.new TreeNode(2);
		root2_1.left = root2_2;
		root2_1.right = root2_3;
		System.out.println(subtree.HasSubtree(root1_1, root2_1));
	}

}
