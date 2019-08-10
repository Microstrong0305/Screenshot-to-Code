package jianzhiOffer;

public class jumpFloor_9_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(JumpFloorII(5));
	}
	
    public static int JumpFloorII(int target) {
    	int result = 1;
    	for(int i=1; i<target; i++) {
    		result = result * 2;
    	}
    	return result;
    }

}
