class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Binary_Sort_Tree:
    def __init__(self, node_list):
        self.root = TreeNode(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    # 插入
    def insert(self, data):
        flag, n, p = self.SearchBST(self.root, self.root, data)
        if not flag:
            new_node = TreeNode(data)
            if data > p.val:
                p.right = new_node
            else:
                p.left = new_node

    # 搜索
    def SearchBST(self, node, parent, key):
        # 递归结束条件
        if not node:
            return False, node, parent

        if node.val == key:
            return True, node, parent

        if key < node.val:
            return self.SearchBST(node.left, node, key)
        else:
            return self.SearchBST(node.right, node, key)


class Solution:

    def __init__(self):
        # 用于保存处理过程中的双向链表的尾结点
        self.pLastNodeInList = None

    def Convert(self, pRootOfTree):
        self.ConvertNode(pRootOfTree)
        # pLastNodeInList指向双向链表的尾节点, 我们需要返回头节点
        pHeadOfList = self.pLastNodeInList
        while pHeadOfList != None and pHeadOfList.left != None:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pNode):
        # 结点为空
        if not pNode:
            return None

        pCurrent = pNode
        # 如果有左子树就先处理左子树
        if pCurrent.left != None:
            self.ConvertNode(pCurrent.left)
        # 将当前结点的前驱指向已经处理好的双向链表（由当前结点的左子树构成）的尾结点
        pCurrent.left = self.pLastNodeInList
        # 如果左子树转换成的双向链表不为空，设置尾结点的后继
        if self.pLastNodeInList != None:
            self.pLastNodeInList.right = pCurrent
            # 记录当前结点为尾结点
        self.pLastNodeInList = pCurrent
        # 处理右子树
        if pCurrent.right != None:
            self.ConvertNode(pCurrent.right)


class Painter:
    def printList(self, head):
        while head != None:
            print(str(head.val) + '->', end='')
            head = head.right

    def printTree(self, root):
        if root != None:
            self.printTree(root.left)
            print(str(root.val) + '->', end='')
            self.printTree(root.right)


if __name__ == "__main__":
    # 构建二叉排序树
    tree = [10, 6, 14, 4, 8, 12, 16]
    binarySortTree = Binary_Sort_Tree(tree)

    print("Before convert: 中序遍历二叉排序树")
    pinter = Painter()
    pinter.printTree(binarySortTree.root)

    sol = Solution()
    head = sol.Convert(binarySortTree.root)

    print("\nAfter convert: 打印出排序后的双向链表")
    pinter.printList(head)
