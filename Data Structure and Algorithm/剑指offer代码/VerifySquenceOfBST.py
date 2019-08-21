'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则输出Yes,否则输出No。假设输入的数组
的任意两个数字都互不相同。
'''


class Solution:

    def VerifySquenceOfBST(self, sequence):
        # 序列为空，返回False
        if not sequence:
            return False
        # 获取序列的长度和二叉搜索树的根节点
        length = len(sequence)
        root = sequence[-1]
        # 寻找二叉搜索树的左子树
        for i in range(length):
            if sequence[i] > root:
                break
        # 判断二叉树右子树中的每一个元素的值是否都比根节点的大
        for j in range(i, length):
            if sequence[j] < root:
                return False
        # 递归调用，分别查看二叉树的左右子树
        left = right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        if i < length - 1 and left:
            right = self.VerifySquenceOfBST(sequence[i: -1])
        # 当左右两个子树都返回True的时候，结果才是True
        return left and right


if __name__ == "__main__":
    sol = Solution()
    # test 1
    # seq = [5, 7, 6, 9, 11, 10, 8]
    # test 2
    seq = [4, 8, 6, 12, 16, 14, 10]
    print(sol.VerifySquenceOfBST(seq))
