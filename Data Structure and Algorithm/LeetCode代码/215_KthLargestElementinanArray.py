from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        :param nums: List[int] 待排序列表
        :param k: int 第k大数值
        :return: int 返回值
        """
        length = len(nums)
        # 构建大顶堆
        for i in range(length // 2 - 1, -1, -1):
            self.adjustHeap(nums, i, length)

        count = 0
        for j in range(length - 1, -1, -1):
            count += 1
            if count == k:
                return nums[0]
            self.swap(nums, 0, j)
            length -= 1
            self.adjustHeap(nums, 0, length)

    def adjustHeap(self, nums, i, length):
        """
        :param nums: 待排序数组
        :param i: 指定以i为根结点排序
        :param length: 待排序数组长度
        :return:
        """
        while True:
            leftChild = i * 2 + 1
            if leftChild >= length:
                return
            if leftChild + 1 < length and nums[leftChild + 1] > nums[leftChild]:
                leftChild += 1
            if nums[leftChild] > nums[i]:
                self.swap(nums, i, leftChild)
                i = leftChild
            else:
                return

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    sol = Solution()
    print(sol.findKthLargest(nums, 2))
