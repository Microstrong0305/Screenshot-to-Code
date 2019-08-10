package jianzhiOffer;

import java.util.Scanner;

public class ugleNum_34 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(GetUglyNumber_Solution(n));
	}
	
	 public static int GetUglyNumber_Solution(int index) {
			int  i = 0;
			int count = 0;
			while(count< index) {
					i++;
					if(isUgleNum(i)) {
						count++;
					}
				}
				return i;
	 }
	
	public static boolean isUgleNum(int num) {
		while(num%2 == 0) {
			num = num /2;
		}
		while(num%3 == 0) {
			num = num /3;
		}
		while(num%5 == 0) {
			num = num /5;
		}
		if(num ==1) {
			return true;
		}else {
			return false;
		}
	}

}
