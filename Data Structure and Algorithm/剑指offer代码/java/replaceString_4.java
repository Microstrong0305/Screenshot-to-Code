package jianzhiOffer;

public class replaceString_4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StringBuffer sb = new StringBuffer("We Are Happy");
		System.out.println(replaceSpace(sb));
	}
	
	public static String replaceSpace(StringBuffer str) {
	 return str.toString().replaceAll("\\s", "%20");
	}

}
