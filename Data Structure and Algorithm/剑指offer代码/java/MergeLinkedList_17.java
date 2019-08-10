package jianzhiOffer;

public class MergeLinkedList_17 {

	// ������
	public class ListNode {
		int val;
		ListNode next = null;

		ListNode(int val) {
			this.val = val;
		}
	}

	// ��������
	public ListNode currentNode = null;
	ListNode head_cre = null;

	public ListNode createList(int val) {
		if (head_cre == null) {
			head_cre = new ListNode(val);
			currentNode = head_cre;
		} else {
			ListNode temp = new ListNode(val);
			currentNode.next = temp;
			currentNode = temp;
		}
		return head_cre;
	}

	// �ϲ�������������
	public ListNode Merge(ListNode list1, ListNode list2) {
		ListNode pc = null; // ���ڼ�¼��ǰ����Ľ��
		ListNode list3 = null; // ��Ҫ���ص�����ͷ����
		if (list1 == null)
			return list2;
		if (list2 == null)
			return list1;
		while (list1 != null && list2 != null) {
			if (list1.val <= list2.val) {
				if (pc == null) {
					pc = list1;
					list3 = pc;
				} else {
					pc.next = list1;
					pc = list1;
				}
				list1 = list1.next;
			} else {
				if (pc == null) {
					pc = list2;
					list3 = pc;
				} else {
					pc.next = list2;
					pc = list2;
				}
				list2 = list2.next;
			}
		}
		if (list1 == null) {
			pc.next = list2;
		} else {
			pc.next = list1;
		}
		return list3;
	}

	// ����������������ӡ������������Ĳ�����ʾ�ӽڵ�node��ʼ���б���
	ListNode current = null;

	public void print(ListNode node) {
		if (node == null) {
			return;
		}

		current = node;
		while (current != null) {
			System.out.println(current.val);
			current = current.next;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MergeLinkedList_17 mg = new MergeLinkedList_17();
		ListNode list1 = null;
		ListNode list2 = null;
		ListNode list3 = null;
		// ��������
		for (int i = 1; i <= 5; i += 2) {
			list1 = mg.createList(i);
		}
		mg.head_cre = null;
		mg.currentNode = null;
		for (int i = 2; i <= 6; i += 2) {
			list2 = mg.createList(i);
		}
		// �ϲ�������������
		list3 = mg.Merge(list1, list2);
		// ��ӡ���ϲ����������
		mg.print(list3);
	}

}
