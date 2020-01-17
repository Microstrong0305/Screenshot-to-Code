package jianzhiOffer;

public class ArrayInversePairs_36 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {7, 5, 6, 4};
		System.out.println(InversePairs(arr));
	}

    public static int InversePairs(int[] array) {
    	
    	if(array == null || array.length <= 0) {
    		return 0;
    	}
    	
    	int[] tmpArr = new int[array.length];
    	for(int i = 0; i < array.length; i++) {
    		tmpArr[i] = array[i];
    	}
    	int count = InversePairsCore(array, tmpArr, 0, array.length - 1);
    	return count;
    }  
    
    public static int InversePairsCore(int[] arr, int[] tmpArr, int low, int high) {
    	if(low == high) {
    		tmpArr[low] = arr[low];
    		return 0;
    	}
    	int len = (high - low) / 2;
    	int left = InversePairsCore(tmpArr, arr, low, low + len) % 1000000007;
    	int right = InversePairsCore(tmpArr, arr, low + len + 1, high) % 1000000007;
    	//p1初始化为前半段最后一个数字的下标
    	int p1 = low + len;
    	//p2 初始化为后半段最后一个数字的下标
    	int p2 = high;
    	// 开始拷贝的位置
    	int p3 = high;
    	// 逆序数
    	int count = 0;
    	while(p1 >= low && p2 >= low + len + 1) {
    		if(arr[p1] > arr[p2]) {
    			//对应的逆序数
    			count += p2 - low - len;
    			tmpArr[p3] = arr[p1];
    			p3--;
    			p1--;
    			if(count >= 1000000007)
    				count %= 1000000007;
    		} else {
    			tmpArr[p3] = arr[p2];
    			p3--;
    			p2--;
    		}
    	}
    	
    	while(p1 >= low) {
    		tmpArr[p3] = arr[p1];
    		p3--;
    		p1--;
    	}
    	
    	while(p2 >= low + len + 1) {
    		tmpArr[p3] = arr[p2];
    		p3--;
    		p2--;
    	}
    	
    	return (count + left + right) % 1000000007;
    }
    
}
