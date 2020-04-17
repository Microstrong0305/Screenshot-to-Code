from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in nums2:
            i = m - 1
            while i > -1:
                if nums1[i] > x:
                    nums1[i + 1] = nums1[i]
                    i -= 1
                else:
                    nums1[i + 1] = x
                    break
            if i == -1:
                nums1[0] = x

            m += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol = Solution()
    print(sol.merge(nums1, m, nums2, n))
