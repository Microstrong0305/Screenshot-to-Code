package jianzhiOffer;

public class reverseLinkedList_16 {
	
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
	
	public ListNode ReverseList(ListNode head) {
		ListNode pReversedHead = null;
		ListNode currentNode = head;
		ListNode preNode = null;
		while(currentNode != null) {
			ListNode nextNode = currentNode.next;
			
			if(nextNode == null) {
				pReversedHead = currentNode;
			}
			
			currentNode.next = preNode;
			preNode = currentNode;
			currentNode = nextNode;
		}
		return pReversedHead;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		reverseLinkedList_16 reverseList = new reverseLinkedList_16();
		for(int i=1; i<=5; i++) {
			reverseList.createLinkedList(i);
		}
		System.out.println(reverseList.ReverseList(reverseList.head).val);
	}

}
