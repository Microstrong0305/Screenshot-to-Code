package jianzhiOffer;

import java.util.HashMap;

public class ConstructTree_6 {
	
	/**
	 * 成员内部类
	 * 二叉树结点
	 */
	public class BinaryTreeNode {
	    public int value;
	    public BinaryTreeNode left = null;
	    public BinaryTreeNode right = null;

	    public BinaryTreeNode() {
	    }

	    public BinaryTreeNode(int data) {
	        this.value = data;
	    }

	    @Override
	    public String toString() {
	        return value + "";
	    }
	}
	
	/**
	 * 根据前序和中序序列（不含有重复的数字），构建一颗二叉树
	 * @param pre 前序序列
	 * @param in  中序序列
	 * @return
	 */
	public static BinaryTreeNode constructBinaryTree(int[] pre, int[] in) {
		
		if(pre == null || in == null || pre.length != in.length || in.length <= 0) {
			return null;
		}
		HashMap<Integer, Integer> map = new HashMap<>();
		for(int i=0; i<in.length; i++) {
			map.put(in[i], i);
		}
		return construct(pre, 0, pre.length-1, in, 0, in.length-1, map);
	}
	
	/**
	 * 
	 * @param pre 前序遍历数组
	 * @param ps  前序遍历开始的位置
	 * @param pe  前序遍历结束的位置
	 * @param in  中序遍历数组
	 * @param is  中序遍历开始的位置
	 * @param ie  中序遍历结束的位置
	 * @param map 中序数组
	 * @return
	 */
	public static BinaryTreeNode construct(int[] pre, int ps, int pe, int[] in, int is, int ie, HashMap<Integer, Integer> map) {
		
		if(ps > pe) {
			//开始位置大于结束位置，说明已经没有需要处理的元素了
			return null;
		}
		
		int value = pre[ps];   //取前序遍历的第一个数字，就是当前的跟节点
		int i = 0;
		try {
			i = map.get(pre[ps]);  //在中序遍历的数组中找根节点的位置
		}catch(Exception e) {
			throw new IllegalArgumentException("Invalid args:前序/中序数组有问题");
		}
		//创建当前根节点
		ConstructTree_6 constructTree = new ConstructTree_6();
		BinaryTreeNode head = constructTree.new BinaryTreeNode(value);
		//递归：
		head.left = construct(pre, ps+1, ps+i-is, in, is, i-1, map);
		head.right = construct(pre, ps+1+i-is, pe, in, i+1, ie, map);
		return head;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
        System.out.println();
	}
	
    // 普通二叉树  
    //              1  
    //           /     \  
    //          2       3  
    //         /       / \  
    //        4       5   6  
    //         \         /  
    //          7       8  
    private static void test1() {
        int[] pre = {1, 2, 4, 7, 3, 5, 6, 8};
        int[] in = {4, 7, 2, 1, 5, 3, 8, 6};
        BinaryTreeNode root = constructBinaryTree(pre, in);
        ConstructTree_6 constructTree1 = new ConstructTree_6();
        PrintBinaryTree printTree = constructTree1.new  PrintBinaryTree();
        printTree.print(root);
    }
    
    /**
     * 打印二叉树
     *
     * Created by nibnait on 2016/9/15.
     */
    public class PrintBinaryTree {

        private static final int NODE_LENGTH = 17;      //二叉树中每个节点的长度

        public void print(BinaryTreeNode head) {

            System.out.println("Binary Tree：");
            printInOrder(head, 0, "*");
            System.out.println();
        }

        private void printInOrder(BinaryTreeNode head, int height, String to) {
            if (head == null){
                return;
            }
            printInOrder(head.left, height+1, "~");
            String val = to + head.value + to;
            int lenM = val.length();
            int lenL = (NODE_LENGTH - lenM) / 2;
            int lenR = NODE_LENGTH - lenL - lenM;
            val = getSpace(height*NODE_LENGTH + lenL) + val + getSpace(lenR);
            System.out.println(val);
            printInOrder(head.right, height+1, "_");
        }

        private String getSpace(int n) {
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < n; i++) {
                sb.append(" ");
            }
            return sb.toString();
        }
    }

}
