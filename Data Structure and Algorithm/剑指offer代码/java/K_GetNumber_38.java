package jianzhiOffer;

public class K_GetNumber_38 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {1, 2, 3, 3, 3, 3, 4, 5};
		System.out.println(GetNumberOfK(arr, 3));
	}
	
    public static int GetNumberOfK(int [] array , int k) {
    	int number = 0;
    	if(array != null && array.length > 0) {
    		int firstK = GetFirstK(array, k, 0, array.length-1);
    		int lastK = GetLastK(array, k, 0,array.length-1);
    		
    		if(firstK > -1 && lastK > -1)
    			number = lastK - firstK + 1;
    	}
    	return number;
    }
    
    /**
     * 求排序数组中的第一个k的下标
     * @param array
     * @param k
     * @param start
     * @param end
     * @return
     */
    public static int GetFirstK(int[] array, int k, int start, int end) {
    	if(start > end)
    		return -1;
    	int middleIndex = (start + end) / 2;
    	int middleData = array[middleIndex];
    	
    	if(middleData == k) {
    		if((middleIndex > 0 && array[middleIndex - 1] != k) || middleIndex == 0)
    			return middleIndex;
    		else
    			end = middleIndex - 1;
    	}else if(middleIndex > k)
    		end = middleIndex - 1;
    	else
    		start = middleIndex + 1;
    	
    	return GetFirstK(array, k, start, end);
    }
    
    /**
     * 求排序数组中的最后一个k的下标
     * @param array
     * @param k
     * @param start
     * @param end
     * @return
     */
    public static int GetLastK(int[] array, int k, int start, int end) {
    	if(start > end)
    		return -1;
    	int middleIndex = (start + end) / 2;
    	int middleData = array[middleIndex];
    	
    	if(middleData == k) {
    		if((middleIndex < array.length - 1 && array[middleIndex + 1] != k) || middleIndex == array.length - 1)
    			return middleIndex;
    		else
    			start = middleIndex + 1;
    	}
    	else if(middleData < k)
    		start = middleIndex + 1;
    	else 
    		end = middleIndex - 1;
    	
    	return GetLastK(array, k, start, end);
    }
}
