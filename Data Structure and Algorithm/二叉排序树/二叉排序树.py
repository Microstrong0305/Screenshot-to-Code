class TreeNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Solution:

    def SearchBST(self, root, key):
        if not root or root.key == key:
            return root
        elif key < root.key:
            return self.SearchBST(root.left, key)
        else:
            return self.SearchBST(root.right, key)


if __name__ == "__main__":
    # 用双向链表构建二叉排序树
    root = TreeNode(10)

    node3 = TreeNode(4, parent=root, left=None, right=None)

    node4 = TreeNode(8, parent=root, left=None, right=None)

    node5 = TreeNode(12, parent=root, left=None, right=None)

    node6 = TreeNode(16, parent=root, left=None, right=None)

    node1 = TreeNode(6, parent=root, left=node3, right=node4)

    node2 = TreeNode(14, parent=root, left=node5, right=node6)

    # 二叉排序树的搜索算法 - 递归写法
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
       
        
        
        
        
        
        
        
        
        
        
        
        
