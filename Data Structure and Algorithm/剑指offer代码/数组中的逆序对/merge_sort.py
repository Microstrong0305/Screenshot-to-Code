class Solution:

    def mergeSort(self, array, low, high):
        mid = (low + high) // 2
        if low < high:
            # 左边
            self.mergeSort(array, low, mid)
            # 右边
            self.mergeSort(array, mid + 1, high)

            # 左右合并
            temp = [0] * (high - low + 1)
            # 左指针
            i = low
            # 右指针
            j = mid + 1
            k = 0
            # 把较小的数先移到新数组中
            while i <= mid and j <= high:
                if array[i] < array[j]:
                    temp[k] = array[i]
                    k += 1
                    i += 1
                else:
                    temp[k] = array[j]
                    k += 1
                    j += 1

            # 把左边剩余的数移入数组中
            while i <= mid:
                temp[k] = array[i]
                k += 1
                i += 1

            # 把右边剩余的数移入到数组中
            while j <= high:
                temp[k] = array[j]
                k += 1
                j += 1

            for i in range(0, len(temp)):
                array[i + low] = temp[i]

        return array


if __name__ == "__main__":
    array = [7, 5, 6, 4]
    sol = Solution()
    print(sol.mergeSort(array, 0, len(array) - 1))
