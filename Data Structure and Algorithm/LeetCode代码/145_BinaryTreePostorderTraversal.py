from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        res = []

        def postorder(root, res):

            if root is None:
                return res

            postorder(root.left, res)

            postorder(root.right, res)

            res.append(root.val)

        postorder(root, res)

        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        '''
        按照根节点，左节点，右节点的顺序入栈，然后逐个添加到res的头部。
        '''
        if root is None:
            return []

        res = list()
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

            res.insert(0, node.val)

        return res

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        '''
        既然后序遍历的顺序是左右中，那么自然地想，可不可以先算出中右左的遍历，然后逆转结果得到后序遍历的结果呢。
        :param root:
        :return:
        '''
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]


if __name__ == "__main__":
    root = TreeNode(1)
    level1_right = TreeNode(2)
    level2_left = TreeNode(3)

    root.right = level1_right
    level1_right.left = level2_left

    sol = Solution()
    print(sol.postorderTraversal3(root))
