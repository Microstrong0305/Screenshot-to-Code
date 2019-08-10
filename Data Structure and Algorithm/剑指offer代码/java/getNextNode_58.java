package jianzhiOffer;

public class getNextNode_58 {
	
	public class TreeLinkNode {
	    int val;
	    TreeLinkNode left = null;
	    TreeLinkNode right = null;
	    TreeLinkNode next = null;

	    TreeLinkNode(int val) {
	        this.val = val;
	    }
	}
	
    public TreeLinkNode GetNext(TreeLinkNode pNode){
    	if(pNode == null) {
    		return null;
    	}
    	TreeLinkNode pNext = null;
    	//1.如果一个结点有右子树，那么它的下一个结点就是它的右子树中的最左子结点。
    	if(pNode.right != null) {
    		TreeLinkNode pRight = pNode.right;
    		while(pRight.left != null)
    			pRight = pRight.left;
    		
    		pNext = pRight;
    	}else if (pNode.next != null) {
			// 2. 程序不进入while循环的话，可以解决：如果结点是它父结点的左子节点，那么它的下一个结点就是它的父节点。
    		TreeLinkNode pCurrent = pNode;
    		TreeLinkNode pParent = pNode.next;
    		while(pParent != null && pCurrent == pParent.right) {
    			//3. 如果一个结点即没有右子树，并且它还是它父结点的右子结点，我们可以沿着指向父结点的指针一直向上
    			//   遍历，直到找到一个是它父结点的左子结点的结点。如果这样的结点存在，那么这个结点的父结点就是我们
    			//   要找的下一个结点。
    			pCurrent = pParent;
    			pParent = pParent.next;
    		}
    		
    		pNext = pParent;
		}
    	
        return pNext;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		                 1
//		               /   \
//		              2     3
//		             / \   / \
//		            4   5 6   7
//		               / \
//		              8   9
		getNextNode_58 getNode = new getNextNode_58();
		TreeLinkNode Node_1 = getNode.new TreeLinkNode(1);
		TreeLinkNode Node_2 = getNode.new TreeLinkNode(2);
		TreeLinkNode Node_3 = getNode.new TreeLinkNode(3);
		TreeLinkNode Node_4 = getNode.new TreeLinkNode(4);
		TreeLinkNode Node_5 = getNode.new TreeLinkNode(5);
		TreeLinkNode Node_6 = getNode.new TreeLinkNode(6);
		TreeLinkNode Node_7 = getNode.new TreeLinkNode(7);
		TreeLinkNode Node_8 = getNode.new TreeLinkNode(8);
		TreeLinkNode Node_9 = getNode.new TreeLinkNode(9);
		Node_1.left = Node_2;
		Node_1.right = Node_3;
		Node_2.left = Node_4;
		Node_2.right = Node_5;
		Node_2.next = Node_1;
		Node_3.left = Node_6;
		Node_3.right = Node_7;
		Node_3.next = Node_1;
		Node_4.next = Node_2;
		Node_5.left = Node_8;
		Node_5.right = Node_9;
		Node_5.next = Node_2;
		Node_6.next = Node_3;
		Node_7.next = Node_3;
		Node_8.next = Node_5;
		Node_9.next = Node_5;
		System.out.println(getNode.GetNext(Node_9).val);
	}

}
