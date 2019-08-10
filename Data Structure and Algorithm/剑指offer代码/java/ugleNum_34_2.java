package jianzhiOffer;

public class ugleNum_34_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(GetUgleNumber_Solution(7));
	}
	
	public static int GetUgleNumber_Solution(int index) {
		if(index <= 0) {
			return 0;
		}
		int[] ugleNumbers = new int[index];
		ugleNumbers[0] = 1;
		
		int Multiply2 = 0;
		int Multiply3 = 0;
		int Multiply5 = 0;
		
		for(int i=1; i<index; i++) {
			int min = Min(ugleNumbers[Multiply2]*2, ugleNumbers[Multiply3]*3, ugleNumbers[Multiply5]*5);
			ugleNumbers[i] = min;
			System.out.println(ugleNumbers[i]);
			while(ugleNumbers[Multiply2]*2 == ugleNumbers[i])
				Multiply2++;
			while(ugleNumbers[Multiply3]*3 == ugleNumbers[i])
				Multiply3++;
			while(ugleNumbers[Multiply5]*5 == ugleNumbers[i])
				Multiply5++;
		}
		return ugleNumbers[index-1];
	}
	
	public static int Min(int number1, int number2, int number3) {
		int min = (number1 < number2) ? number1 :  number2;
		min = (min < number3) ? min : number3;
		return min;
	}

}
