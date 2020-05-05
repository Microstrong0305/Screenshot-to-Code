class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        