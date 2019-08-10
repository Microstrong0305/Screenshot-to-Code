package jianzhiOffer;

import java.util.HashMap;

public class ConstructTree_6 {
	
	/**
	 * ��Ա�ڲ���
	 * ���������
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
	 * ����ǰ����������У��������ظ������֣�������һ�Ŷ�����
	 * @param pre ǰ������
	 * @param in  ��������
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
	 * @param pre ǰ���������
	 * @param ps  ǰ�������ʼ��λ��
	 * @param pe  ǰ�����������λ��
	 * @param in  �����������
	 * @param is  ���������ʼ��λ��
	 * @param ie  �������������λ��
	 * @param map ��������
	 * @return
	 */
	public static BinaryTreeNode construct(int[] pre, int ps, int pe, int[] in, int is, int ie, HashMap<Integer, Integer> map) {
		
		if(ps > pe) {
			//��ʼλ�ô��ڽ���λ�ã�˵���Ѿ�û����Ҫ�����Ԫ����
			return null;
		}
		
		int value = pre[ps];   //ȡǰ������ĵ�һ�����֣����ǵ�ǰ�ĸ��ڵ�
		int i = 0;
		try {
			i = map.get(pre[ps]);  //������������������Ҹ��ڵ��λ��
		}catch(Exception e) {
			throw new IllegalArgumentException("Invalid args:ǰ��/��������������");
		}
		//������ǰ���ڵ�
		ConstructTree_6 constructTree = new ConstructTree_6();
		BinaryTreeNode head = constructTree.new BinaryTreeNode(value);
		//�ݹ飺
		head.left = construct(pre, ps+1, ps+i-is, in, is, i-1, map);
		head.right = construct(pre, ps+1+i-is, pe, in, i+1, ie, map);
		return head;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		test1();
        System.out.println();
	}
	
    // ��ͨ������  
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
     * ��ӡ������
     *
     * Created by nibnait on 2016/9/15.
     */
    public class PrintBinaryTree {

        private static final int NODE_LENGTH = 17;      //��������ÿ���ڵ�ĳ���

        public void print(BinaryTreeNode head) {

            System.out.println("Binary Tree��");
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
