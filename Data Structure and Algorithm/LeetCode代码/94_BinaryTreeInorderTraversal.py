from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []

        def inorderTree(root, res):

            if root is None:
                return res

            if root.left is not None:
                inorderTree(root.left, res)

            res.append(root.val)

            if root.right is not None:
                inorderTree(root.right, res)

        inorderTree(root, res)

        return res

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res, stack = [], []
        stack.append(root)
        while stack:
            while root and root.left:
                stack.append(root.left)
                root = root.left

            root = stack.pop()
            res.append(root.val)

            root = root.right

            if root:
                stack.append(root)

        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


if __name__ == "__main__":
    root = TreeNode(1)
    level1_right = TreeNode(2)
    level2_left = TreeNode(3)

    root.right = level1_right
    level1_right.left = level2_left

    sol = Solution()
    print(sol.inorderTraversal2(root))
