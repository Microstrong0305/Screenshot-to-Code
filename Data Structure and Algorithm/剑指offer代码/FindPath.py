'''
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点
所经过的结点形成一条路径。(注意：在返回值的list中，数组长度大的数组靠前)

思路：递归先序遍历树，把结点加入路径。使用列表结构存树结构
若该结点是叶子结点则比较当前路径和是否等于期待和，叶子节点说明该路径应该截止了
弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

     # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        res = []
        path = []
        self.subPath(root, res, path, expectNumber, 0)
        return res

    def subPath(self, root, res, path, expectNumber, currentNum):
        currentNum += root.val
        # root使用append转换成了列表，因为最后要一个序列，root本身还是树节点结构
        path.append(root)
        # 判断是不是到叶子节点了，到叶子节点了就要判断值的和是不是相等
        if not root.left and not root.right:
            if currentNum == expectNumber:
                onePath = []
                for node in path:
                    onePath.append(node.val)
                res.append(onePath)
        if currentNum < expectNumber:
            if root.left:
                self.subPath(root.left, res, path, expectNumber, currentNum)
            if root.right:
                self.subPath(root.right,res, path, expectNumber, currentNum)

        # 拿到一个正确的路径后要弹出，回到上一次父节点继续递归
        path.pop()

if __name__ == "__main__":
    sol = Solution()
    n1 = TreeNode(10)
    n2 = TreeNode(5)
    n3 = TreeNode(12)
    n4 = TreeNode(4)
    n5 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print(sol.FindPath(n1, 22))

'''
Reference:
【1】https://drivingc.com/p/5c75fd134b0f2b0a081321e3#34.%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84
【2】https://github.com/leeguandong/Interview-code-practice-python/blob/master/%E5%89%91%E6%8C%87offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.py
'''



