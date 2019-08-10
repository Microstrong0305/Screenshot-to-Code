package jianzhiOffer;

import java.util.Stack;

public class stackAchieveQueue_7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		stackAchieveQueue_7 saq = new stackAchieveQueue_7();
		for(int i=0; i<5; i++) {
			saq.push(i);
		}
		for(int j=0; j<5; j++) {
		System.out.println(saq.pop());
		}
	}
	
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void push(int node) {
    	stack1.push(node);
    }
    
    public int pop() {
    	if(stack1.isEmpty() && stack2.isEmpty()) {
    		throw new RuntimeException("Queue is empty!");
    	}
    	if(stack2.isEmpty()) {
    		while(!stack1.isEmpty()) {
    			stack2.push(stack1.pop());
    		}
    	}
    	return stack2.pop();
    }

}
