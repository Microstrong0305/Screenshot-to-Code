class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 树的最大深度
    # 非递归解法-深度优先遍历DFS
    def maxDepth(self, root):
        if not root:
            return 0

        stack = []
        currentDepth = 1
        stack.append((root, currentDepth))
        getMaxDepth = 1
        while stack:
            node, currentDepth = stack.pop()
            getMaxDepth = max(getMaxDepth, currentDepth)
            if node.left:
                stack.append((node.left, currentDepth + 1))
            if node.right:
                stack.append((node.right, currentDepth + 1))

        return getMaxDepth

    # 树的最大深度
    # 递归解法
    def maxDepth1(self, root):
        if not root:
            return 0

        def getMaxDepth(node):
            if not node:
                return 0

            left = getMaxDepth(node.left)

            right = getMaxDepth(node.right)

            return max(left, right) + 1

        return getMaxDepth(root)

    # 先序遍历 - 非递归
    def perorderTraversal(self, root):
        if not root:
            return []

        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # 中序遍历- 非递归
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            while root.left:
                root = root.left
                stack.append(root)

            root = stack.pop()
            res.append(root.val)

            if root.right:
                root = root.right
                stack.append(root)
        return res

    # 后序遍历 - 非递归
    def postorderTraversal(self, root):
        if not root:
            return []

        stack = []
        res = []
        stack.append(root)
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return res[::-1]


if __name__ == "__main__":
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    sol = Solution()
    # 二叉树的最大深度 - 非递归解法
    # print(sol.maxDepth(root))

    # 二叉树的最大深度 - 递归解法
    # print(sol.maxDepth1(root))

    # 二叉树的先序遍历 - 非递归解法
    # print(sol.perorderTraversal(root))

    # 二叉树的中序遍历 - 非递归解法
    # print(sol.inorderTraversal(root))

    # 二叉树的后续遍历 - 非递归解法
    print(sol.postorderTraversal(root))
