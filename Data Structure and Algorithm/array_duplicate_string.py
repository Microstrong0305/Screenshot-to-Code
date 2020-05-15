class Solution:

    def is_duplicate_string(self, nums):
        if len(nums) <= 0:
            return True
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return False

        return True

    def is_duplicate_string2(self, nums):
        if len(nums) <= 0:
            return True

        dic = {}
        for i in nums:
            if i in dic.keys():
                return False
            else:
                dic[i] = 1

        return True


if __name__ == "__main__":
    nums = ["abc", "Microstrong", "xyz", "edf", "Microstrong"]
    sol = Solution()
    print(sol.is_duplicate_string2(nums))
