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


if __name__ == "__main__":
    root = TreeNode(1)
    level1_right = TreeNode(2)
    level2_left = TreeNode(3)

    root.right = level1_right
    level1_right.left = level2_left

    sol = Solution()
    print(sol.preorderTraversal(root))
