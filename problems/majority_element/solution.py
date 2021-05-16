class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m, x = nums.pop(0), 1
        for i in nums:
            x += 1 if i == m else -1
            if x <= 0: 
                m, x = i, 1
        return m 
            
