'''
思路：用队列实现

           1、root为空，则返回空表

           2、队列不为空，记下此时队列中的结点个数length，length个结点出队列的同时，记录结点值，并把结点的左右子结点加入队列
'''

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        res = []
        # 如果根结点为空，则返回空列表
        if root is None:
            return res
        # 模拟一个队列存储节点
        queue = []
        # 首先将根节点入队
        queue.append(root)
        # 列表为空时，循环终止
        while len(queue) != 0:
            # 使用列表存储同层节点
            levelValue = []
            # 记录同层节点的个数
            length = len(queue)
            for i in range(length):
                # 将同层节点依次出队
                temp = queue.pop(0)
                # 非空左孩子入队
                if temp.left is not None:
                    queue.append(temp.left)
                # 非空右孩子入队
                if temp.right is not None:
                    queue.append(temp.right)

                levelValue.append(temp.val)

            res.append(levelValue)
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    level1_left = TreeNode(9)
    level1_right = TreeNode(20)
    root.left = level1_left
    root.right = level1_right

    level2_left = TreeNode(15)
    level2_right = TreeNode(7)
    level1_right.left = level2_left
    level1_right.right = level2_right

    sol = Solution()
    print(sol.levelOrder(root))

'''
Reference：
【1】https://blog.csdn.net/weixin_40314737/article/details/80942856
【2】https://blog.csdn.net/yurenguowang/article/details/76906620
'''
