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

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heapreplace
        # 使用大顶堆
        heap = []
        for i in range(len(nums)):
            if i < k:
                heappush(heap, nums[i])  # 将 nums[i] 压入堆中
            else:
                if nums[i] > heap[0]:
                    m = heapreplace(heap, nums[i])  # 弹出最小的元素，并将nums[i]压入堆中，返回弹出的元素
        return heap[0]

    def findKthLargest3(self, nums: List[int], k: int) -> int:

        low, high = 0, len(nums) - 1

        def select_k(nums, low, high, k):
            if low == high:
                return nums[low]
            partitionIndex = self.partition(nums, low, high)
            index = high - partitionIndex + 1  # 找到的是第几大的值
            if index == k:
                return nums[partitionIndex]
            elif index < k:
                # 此时向左查找
                return select_k(nums, low, partitionIndex - 1, k - index)
            else:
                return select_k(nums, partitionIndex + 1, high, k)

        return select_k(nums, low, high, k)

    def partition(self, nums, low, high):
        pivot = nums[low]
        while low < high:
            while low < high and pivot <= nums[high]:
                high -= 1
            nums[low] = nums[high]
            while low < high and pivot > nums[low]:
                low += 1
            nums[high] = nums[low]

        nums[high] = pivot

        return high


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    sol = Solution()
    print(sol.findKthLargest3(nums, 2))
