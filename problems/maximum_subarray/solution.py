class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                self.check_if_max_sum(curr_sum)
                curr_sum = 0
            elif curr_sum >= 0 and nums[i] < 0:
                self.check_if_max_sum(curr_sum)
            curr_sum += nums[i]
        self.check_if_max_sum(curr_sum)
        return self.max_sum
    
    def check_if_max_sum(self,curr_sum):
        if curr_sum > self.max_sum:
            self.max_sum = curr_sum

        