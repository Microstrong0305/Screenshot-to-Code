package jianzhiOffer;

public class GetLeastNumbers_30_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {79, 66, 43, 83, 30, 87, 38, 55};
		HeapSort(arr);
		for (int i : arr) {
			System.out.println(i);
		}
	}
	
	 public static void HeapSort(int[] a) {
	        // 初始建堆
	        for (int i=a.length/2-1; i>=0; i--) {     //从最后一个非叶子节点开始，从左向右，从下往上，调整成大顶堆
	        	HeapAdjust(a, i, a.length);
	        }
	        // 交换元素后，调整堆
	        for (int i=a.length-1; i>0; i--) {
	            swapReferences(a, 0, i);       // 调整堆顶元素与末尾元素
	            HeapAdjust(a, 0, i);               // 重新调整（堆顶），堆的范围是length - 1, 最后一个元素已经从堆中排除
	        }
	    }
	 
	 /**
	  * 在数组中交换两个元素
	  * @param a 数组
	  * @param index1 下标1
	  * @param index2 下标2
	  */
	 public static void swapReferences(int[] a, int index1, int index2) {
		 int tmp = a[index1];
		 a[index1] = a[index2];
		 a[index2] = tmp;
	 }
	 
   /**
     * 调整堆的思路：从序号最大的非叶子节点开始便利，左右孩子中有比它大的，交换该节点和叶子的位置
     * 父节点和较大的孩子节点交换后，新的父节点是稳定的，但是新的孩子节点可能不满足大顶堆规则，而另一边的孩子不会受影响，
     * 所以要继续对新孩子进行调整判断，直至新孩子满足规则，或者没有新孩子为止
     */
    public static void HeapAdjust(int[] a, int i, int n) {
        int child;
        int tmp; // 保存待调整的父亲节点
        // 从最后一个非叶子节点开始
        for (tmp = a[i]; leftChild(i) < n; i=child) { // 交换以后，调下去的节点可能会依旧不平衡
            child = leftChild(i);   // 取得左孩子的下标
            //child=n-1, 说明只有一个左孩子，直接到下一步
            if (child != n - 1 && a[child] < a[child+1]) { //找出两个孩子中较大的
                child++;
            }
            if (tmp < a[child]) {  //如果堆顶小于比较大的孩子，交换位置
                a[i] = a[child];
            } else {
                break;
            }
        }
        a[i] = tmp;     // 父节点元素给child
    }
    
    public static int leftChild(int i) {
        return 2 * i + 1;
    }

}
