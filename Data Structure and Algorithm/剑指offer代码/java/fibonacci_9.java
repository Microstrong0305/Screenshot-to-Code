package jianzhiOffer;

import java.util.Arrays;

public class fibonacci_9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(Fibonacci(7));
	}
	
    public static int Fibonacci(int n) {
    	if(n == 0)
    		return 0;
    	else if(n == 1 || n == 2)
    		return 1;
    	else {
        	int[] memo = new int[n+1];
        	Arrays.fill(memo, -1);
        	memo[0] = 0;
        	memo[1] = 1;
        	memo[2] = 1;
        	for(int i=3; i<=n; i++) {
        		if(memo[i] == -1)
        			memo[i] = memo[i-1] + memo[i-2];
        	}
        	return memo[n];
		}
    }

}
