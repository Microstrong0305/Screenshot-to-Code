package jianzhiOffer;

public class SolutionFind {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
      int target = 7;
      int[][] array = {{1,2,8,9},{2,4,9,12},{4,7,10,13},{6,8,11,15}};
      Find(target,array);
	}
	//时间复杂度是O(n^2)
//	public static boolean Find(int target,int[][] array) {
//		int row = array.length;
//		int col = array[row].length;
//		for(int i=0; i<row; i++) {
//			for(int j=0; j<col; j++) {
//				if(array[i][j]==target) {
//					return true;
//				}
//			}
//		}
//		return false;
//	}
	
	//时间复杂度为O(nlogn)
//	public static boolean Find(int target,int[][] array) {
//		int row = array.length;
//		for(int i=0; i<row; i++) {
//			int high = array[i].length-1;
//			int low =0; 
//			while(low<=high) {
//				int mid = (low+high)/2;
//				if(array[i][mid]==target)
//					return true;
//				else if(array[i][mid]<target) {
//					low = mid +1;
//				}else {
//					high = mid -1;
//				}
//			}
//		}
//		return false;
//	}
	
	public static boolean Find(int target,int[][] array) {
		int row = array.length;
		int col = array[0].length;
		int i = row-1;
		int j = 0;
		while(i>=0&&i<row&&j<col) {
			if(array[i][j]==target) {
				return true;
			}else if(array[i][j]>target){
					i--;
			}else {
					j++;
			}
		}
		return false;
	}

}
