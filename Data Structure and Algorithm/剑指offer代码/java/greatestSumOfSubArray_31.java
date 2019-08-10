package jianzhiOffer;

public class greatestSumOfSubArray_31 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {-2, -8, -1, -5, -9};
		int[] arr1 = {1, -2, 3, 10, -4, 7, 2, -5};
		System.out.println(FindGreatestSumOfSubArray(arr1));
	}
	
    public static int FindGreatestSumOfSubArray(int[] array) {
    	int maxSum = Integer.MIN_VALUE;
    	int currentSum = 0;
    	for(int i=0; i<array.length; i++) {
    		if(currentSum <= 0) {
    			currentSum = array[i];
    		}else {
    			currentSum += array[i];
    		}
    		if(currentSum > maxSum) {
    			maxSum = currentSum;
    		}
    	}
    	return maxSum;
    }

}
