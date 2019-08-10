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
	        // ��ʼ����
	        for (int i=a.length/2-1; i>=0; i--) {     //�����һ����Ҷ�ӽڵ㿪ʼ���������ң��������ϣ������ɴ󶥶�
	        	HeapAdjust(a, i, a.length);
	        }
	        // ����Ԫ�غ󣬵�����
	        for (int i=a.length-1; i>0; i--) {
	            swapReferences(a, 0, i);       // �����Ѷ�Ԫ����ĩβԪ��
	            HeapAdjust(a, 0, i);               // ���µ������Ѷ������ѵķ�Χ��length - 1, ���һ��Ԫ���Ѿ��Ӷ����ų�
	        }
	    }
	 
	 /**
	  * �������н�������Ԫ��
	  * @param a ����
	  * @param index1 �±�1
	  * @param index2 �±�2
	  */
	 public static void swapReferences(int[] a, int index1, int index2) {
		 int tmp = a[index1];
		 a[index1] = a[index2];
		 a[index2] = tmp;
	 }
	 
   /**
     * �����ѵ�˼·����������ķ�Ҷ�ӽڵ㿪ʼ���������Һ������б�����ģ������ýڵ��Ҷ�ӵ�λ��
     * ���ڵ�ͽϴ�ĺ��ӽڵ㽻�����µĸ��ڵ����ȶ��ģ������µĺ��ӽڵ���ܲ�����󶥶ѹ��򣬶���һ�ߵĺ��Ӳ�����Ӱ�죬
     * ����Ҫ�������º��ӽ��е����жϣ�ֱ���º���������򣬻���û���º���Ϊֹ
     */
    public static void HeapAdjust(int[] a, int i, int n) {
        int child;
        int tmp; // ����������ĸ��׽ڵ�
        // �����һ����Ҷ�ӽڵ㿪ʼ
        for (tmp = a[i]; leftChild(i) < n; i=child) { // �����Ժ󣬵���ȥ�Ľڵ���ܻ����ɲ�ƽ��
            child = leftChild(i);   // ȡ�����ӵ��±�
            //child=n-1, ˵��ֻ��һ�����ӣ�ֱ�ӵ���һ��
            if (child != n - 1 && a[child] < a[child+1]) { //�ҳ����������нϴ��
                child++;
            }
            if (tmp < a[child]) {  //����Ѷ�С�ڱȽϴ�ĺ��ӣ�����λ��
                a[i] = a[child];
            } else {
                break;
            }
        }
        a[i] = tmp;     // ���ڵ�Ԫ�ظ�child
    }
    
    public static int leftChild(int i) {
        return 2 * i + 1;
    }

}
