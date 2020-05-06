from typing import List


class Solution(object):

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        seen = set()
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                for k in range(length):
                    if j == k:
                        continue
                    if i == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        hsh = tuple(sorted(temp))
                        if hsh not in seen:
                            res.append(temp)
                            seen.add(hsh)

        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        '''
        解题思路：
        1，先将数组排序。
　　　　2，排序后，可以按照TwoSum的思路来解题。怎么解呢？可以将num[i]的相反数即-num[i]作为target，然后从i+1到len(num)-1的数组元素中寻找两个数使它们的和为-num[i]就可以了。下标i的范围是从0到len(num)-3。
        3，这个过程要注意去重。
        4，时间复杂度为O(N^2)。
        :param nums:
        :return:
        '''
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        left += 1
                    else:
                        right -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum2(nums))

'''
Reference:
【1】https://www.cnblogs.com/zuoyuan/p/3699159.html
'''
