class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_target = target - nums[i]
            new_list = nums[i + 1:]
            if new_target in new_list:
                return [i, new_list.index(new_target) + i + 1]