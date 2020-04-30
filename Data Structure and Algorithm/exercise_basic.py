class Solution:

    def binSearch(self, nums, target):
        if len(nums) <= 0:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return -1

    def sortArray(self, nums):
        if len(nums) <= 0:
            return nums

        left, right = 0, len(nums) - 1

        def quickSort(nums, left, right):
            if left < right:
                partitionIndex = self.partition(nums, left, right)
                quickSort(nums, left, partitionIndex - 1)
                quickSort(nums, partitionIndex + 1, right)

        quickSort(nums, left, right)

        return nums

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

    def mergeSortArry(self, nums):
        if len(nums) <= 0:
            return nums

        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, low, high):
        mid = (low + high) // 2
        if low < high:
            # 左边
            self.mergeSort(nums, low, mid)
            # 右边
            self.mergeSort(nums, mid + 1, high)
            # 左右合并
            temp = [0] * (high - low + 1)
            # 左指针
            i = low
            # 右指针
            j = mid + 1
            k = 0
            # 把较小的数先移动到新的数组中
            while i <= mid and j <= high:
                if nums[i] < nums[j]:
                    temp[k] = nums[i]
                    k += 1
                    i += 1
                else:
                    temp[k] = nums[j]
                    k += 1
                    j += 1

            # 把左边剩余的数移入数组中
            while i <= mid:
                temp[k] = nums[i]
                k += 1
                i += 1

            # 把右边剩余的数移入到数组中
            while j <= high:
                temp[k] = nums[j]
                k += 1
                j += 1

            # 把临时数组里排好序的数放回原数组中
            for i in range(0, len(temp)):
                nums[i + low] = temp[i]

        return nums


if __name__ == "__main__":
    sol = Solution()
    # 1. 二分查找
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 0
    # print(sol.binSearch(nums, target))
    # 2. 快速排序
    # nums = [5, 1, 1, 2, 0, 0]
    # print(sol.sortArray(nums))
    # 3. 归并排序
    nums = [7, 5, 6, 4]
    print(sol.mergeSortArry(nums))
