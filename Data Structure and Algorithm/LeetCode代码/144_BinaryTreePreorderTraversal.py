from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []

        def preorderTree(root, res):
            if root is None:
                return res

            res.append(root.val)

            if root.left != None:
                preorderTree(root.left, res)

            if root.right != None:
                preorderTree(root.right, res)

        preorderTree(root, res)

        return res

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        迭代方法的需要使用栈，先把右孩子进栈，再左孩子进栈。
        步骤：
        1.根节点入栈。
        2.取出根节点，值加入结果，然后先加右孩子，后加左孩子。
        3.重复2
        :param root:
        :return:
        """
        if not root:
            return []

        res = []

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return res


if __name__ == "__main__":
    root = TreeNode(1)
    level1_right = TreeNode(2)
    level2_left = TreeNode(3)

    root.right = level1_right
    level1_right.left = level2_left

    sol = Solution()
    print(sol.preorderTraversal1(root))
