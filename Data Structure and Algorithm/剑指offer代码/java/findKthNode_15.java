package jianzhiOffer;

public class findKthNode_15 {
	
	class ListNode{
		int val;
		ListNode next = null;
		
		public ListNode(int data) {
			this.val = data;
		}
	}
	
	public ListNode head;
	
	public void createLinkedList(int data) {
		if(head == null) {
			head = new ListNode(data);
		}else {
			ListNode node = new ListNode(data);
			node.next = head;
			head = node;
		}
	}
    
    public ListNode FindKthToTail(ListNode head,int k) {
    	if(head == null || k == 0) {
    		return null;
    	}
    	ListNode p1 = head;
    	ListNode p2 = null;
    	for(int i=0; i<k-1; i++) {
    		if(p1.next != null) {
    			p1 = p1.next;
    		}else {
    			return null;
    		}
    	}
    	p2 = head;
    	while(p1.next!=null) {
    		p1 = p1.next;
    		p2 = p2.next;
    	}
    	return p2;
    }

	public static void main(String[] args) {
		findKthNode_15 list = new findKthNode_15();
		for(int i=0; i<10; i++) {
			list.createLinkedList(i);
		}
		System.out.println(list.FindKthToTail(list.head, 10).val);
	}

}
