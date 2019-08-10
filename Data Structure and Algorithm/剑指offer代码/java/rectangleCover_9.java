package jianzhiOffer;

import java.util.Arrays;

public class rectangleCover_9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(RectCover(33));
	}
	
	public static int[] memo;
	
    public static int RectCover(int target) {
    	memo = new int[target + 1];
    	Arrays.fill(memo, -1);
    	return coverNum(target);
    }
    
    public static int coverNum(int n) {
		if(memo[n] != -1)
			return memo[n];
		else if(n == 0)
    		memo[0] = 0; 
    	else if(n == 1)
    		memo[1] = 1;
    	else if(n == 2)
    		memo[2] = 2;
    	else {
				memo[n] = coverNum(n-1) + coverNum(n-2);
		}
		return memo[n];
    }

}
