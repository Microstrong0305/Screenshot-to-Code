class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBTwithPreMid(self, pre, mid):
        if len(pre) == 0 or len(mid) == 0:
            return None

        root = TreeNode(pre[0])
        for index, item in enumerate(mid):
            if root.val == item:
                root.left = self.getBTwithPreMid(pre[1:index+1], mid[:index])
                root.right = self.getBTwithPreMid(pre[index+1:], mid[index+1:])
                return root

    def print_in_one_line(self, root):
        ''' 打印在一行内，不换行 '''
        if not root:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.val, end=" ")  # end属性默认为“\n”，所以print()函数默认会换行。此处设为空格“ ”，防止自动换行
            if node.left:
                queue.append(node.left)  # 将本节点的左子节点入队
            if node.right:
                queue.append(node.right)  # 将本节点的右子节点入队

    #方法一：
    #思路：递归思想，先交换根节点的左右子树的位置，然后向下递归，把左右子树的根节点作为下次循环的根节点。
    def Mirror(self, root):
        if root == None:
            return None
        root.right, root.left = root.left, root.right
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)

if __name__ == "__main__":
    sol = Solution()
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot = sol.getBTwithPreMid(preorder_seq, middleorder_seq)
    print("由前序和中序构造出的二叉树：")
    sol.print_in_one_line(treeRoot)
    print("\n")
    sol.Mirror(treeRoot)
    print("二叉树的镜像为:")
    sol.print_in_one_line(treeRoot)

'''
Reference:
[1] https://blog.csdn.net/qq_20011607/article/details/89142173
[2] https://blog.csdn.net/u010005281/article/details/79473690
'''



