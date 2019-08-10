package jianzhiOffer;

public class firstCommonNode_37 {
	
	class ListNode{
		int val;
		ListNode next = null;
		
		public ListNode(int val) {
			// TODO Auto-generated constructor stub
			this.val = val;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		firstCommonNode_37 ownClass = new firstCommonNode_37();
		ListNode l1_one = ownClass.new ListNode(1);
		ListNode l1_two = ownClass.new ListNode(2);
		l1_one.next = l1_two;
		ListNode l1_thr = ownClass.new ListNode(3);
		l1_two.next = l1_thr;
		ListNode l1_for = ownClass.new ListNode(6);
		l1_thr.next = l1_for;
		ListNode l1_fiv = ownClass.new ListNode(7);
		l1_for.next = l1_fiv;
		
		ListNode l2_one = ownClass.new ListNode(4);
		ListNode l2_two = ownClass.new ListNode(5);
		l2_one.next = l2_two;
		l2_two.next = l1_for;
		
		ListNode node = FindFirstCommonNode(l1_one, l2_two);
		System.out.println(node.val);
	}
	
	public static ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
		//得到两个链表的长度
		int nLength1 = getListLength(pHead1);
		int nLength2 = getListLength(pHead2);
		//得到两个链表长度之间的差值
		int nLengthDif = nLength1 - nLength2;
		
		ListNode pListHeadLong = null;
		ListNode pListHeadShort = null;
		if(nLengthDif >=0) {
			pListHeadLong = pHead1;
			pListHeadShort = pHead2;
		}else {
			pListHeadLong = pHead2;
			pListHeadShort = pHead1;
			nLengthDif = nLength2 - nLength1;
		}
		
		// 先在长链表上走几步，再同时在两个链表上遍历
		for(int i=0; i<nLengthDif; i++) {
			pListHeadLong = pListHeadLong.next;
		}
		
		// 同时在两个链表上遍历
		while((pListHeadLong != null) && (pListHeadShort != null) && (pListHeadLong != pListHeadShort)) {
			pListHeadLong = pListHeadLong.next;
			pListHeadShort = pListHeadShort.next;
		}
		
		//得到第一个公共结点
		ListNode pFirstCommonNode = pListHeadLong;
		return pFirstCommonNode;
	}
	
	public static int getListLength(ListNode pHead) {
		int nLength = 0;
		ListNode pNode = pHead;
		while(pNode != null) {
			nLength++;
			pNode = pNode.next;
		}
		return nLength;
	}

}
