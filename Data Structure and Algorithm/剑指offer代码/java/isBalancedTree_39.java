package jianzhiOffer;

public class isBalancedTree_39 {
	
	class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		
		public TreeNode(int data) {
			this.val = data;
		}
	}
	
	/**
	 * 树的后序遍历递归实现
	 * @param root
	 */
	public void postOrder(TreeNode root) {
		if(root != null) {
			postOrder(root.left);
			postOrder(root.right);
			System.out.println(root.val);
		}
	}
	
	public boolean IsBalanced_Solution(TreeNode root) {
		int[] depth = new int[] {0};
		return isBalanced(root, depth);
	}
	
	public boolean isBalanced(TreeNode root, int[] depth) {
		if(root == null) {
			depth[0] = 0;
			return true;
		}
		int[] left = new int[] {0};
		int[] right = new int[] {0};
		if(isBalanced(root.left, left) && isBalanced(root.right, right)) {
			int diff = left[0] - right[0];
			if(diff <= 1 && diff >= -1) {
				depth[0] = 1 +(left[0] > right[0] ? left[0] : right[0]);
				return true;
			}
		}
		return false;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 构建树
		//        1
		//       / \
		//      2   3
		//     / \   \
		//    4   5   6
		//       /
		//       7		           
		isBalancedTree_39 balancedTree  = new isBalancedTree_39();
		TreeNode node_1 = balancedTree.new TreeNode(1);
		TreeNode node_2 = balancedTree.new TreeNode(2);
		TreeNode node_3 = balancedTree.new TreeNode(3);
		TreeNode node_4 = balancedTree.new TreeNode(4);
		TreeNode node_5 = balancedTree.new TreeNode(5);
		TreeNode node_6 = balancedTree.new TreeNode(6);
		TreeNode node_7 = balancedTree.new TreeNode(7);
		node_1.left = node_2;
		node_1.right = node_3;
		node_2.left = node_4;
		node_2.right = node_5;
		node_3.right = node_6;
		node_5.left = node_7;
//		balancedTree.postOrder(node_1);
		System.out.println(balancedTree.IsBalanced_Solution(node_1));
	}

}
