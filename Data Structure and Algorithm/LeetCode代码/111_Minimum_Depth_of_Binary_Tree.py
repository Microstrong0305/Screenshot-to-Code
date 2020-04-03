class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        def getDepth(node):

            if not node:
                return 0

            if not node.left:
                return getDepth(node.right) + 1

            elif not node.right:
                return getDepth(node.left) + 1

            else:
                return min(getDepth(node.left), getDepth(node.right)) + 1

        return getDepth(root)


if __name__ == "__main__":
    root = TreeNode(3)

    level1_left = TreeNode(2)
    level2_left = TreeNode(3)

    root.left = level1_left
    level1_left.left = level2_left

    # level1_left = TreeNode(9)
    # level1_right = TreeNode(20)
    #
    # level2_left = TreeNode(15)
    # level2_right = TreeNode(7)
    #
    # root.left = level1_left
    # root.right = level2_right
    #
    # level1_right = level2_left
    # level1_right = level2_right

    sol = Solution()
    print(sol.minDepth(root))
