
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def PrintFromTopToBottom(self, root):
        # 当节点非空时才进行操作
        if not root:
            return []

        if root != None:
            # 用于存放还未遍历的元素
            list = []
            # 用于存放最终的结果
            result = []
            # 将根节点入队
            list.append(root)
            # 队列非空则进行处理
            while list:
                # 删除队首元素
                curNode = list.pop(0)
                # 输出队首元素的值
                result.append(curNode.val)
                # 如果左子结点不为空，则左子节点入队
                if curNode.left != None:
                    list.append(curNode.left)
                # 如果右子节点不为空，则右子节点入队
                if curNode.right != None:
                    list.append(curNode.right)
        return result

if __name__ == "__main__":

#----------------------测试用例1-------------------------------------------------
#            8
#          / \
#        6    10
#      /  \   / \
#    5   7   9  11

    # root = TreeNode(8)
    #
    # root.left = TreeNode(6)
    #
    # root.right = TreeNode(10)
    #
    # root.left.left = TreeNode(5)
    #
    # root.left.right = TreeNode(7)
    #
    # root.right.left = TreeNode(9)
    #
    # root.right.right = TreeNode(11)

#----------------------测试用例2-------------------------------------------------
#                1
#              /
#            3
#          /
#        5
#      /
#     7
#    /
#  9

    # root = TreeNode(1)
    #
    # root.left = TreeNode(3)
    #
    # root.left.left = TreeNode(5)
    #
    # root.left.left.left = TreeNode(7)
    #
    # root.left.left.left.left = TreeNode(9)

#----------------------测试用例3-------------------------------------------------
#            0
#            \
#             2
#              \
#               4
#                \
#                 8

    root = TreeNode(0)

    root.right = TreeNode(2)

    root.right.right = TreeNode(4)

    root.right.right.right = TreeNode(6)

    root.right.right.right.right = TreeNode(8)

    sol = Solution()
    print(sol.PrintFromTopToBottom(root))

# Reference
#[1] https://wiki.jikexueyuan.com/project/for-offer/question-twenty-three.html