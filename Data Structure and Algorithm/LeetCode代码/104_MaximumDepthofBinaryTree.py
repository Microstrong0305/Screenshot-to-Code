from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def getDepth(root):

            if root is None:
                return 0

            left_high = getDepth(root.left)

            right_high = getDepth(root.right)

            return max(left_high, right_high) + 1

        return getDepth(root)

    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(1, root)]

        depth = 0

        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth


if __name__ == "__main__":
    root = TreeNode(3)

    L1 = TreeNode(9)
    R1 = TreeNode(20)

    L2 = TreeNode(20)
    R2 = TreeNode(7)

    root.left = L1
    root.right = R1

    R1.left = L2
    R1.right = R2

    sol = Solution()
    print(sol.maxDepth2(root))
