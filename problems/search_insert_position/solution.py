class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            i = target - 1
            while i not in nums:
                i -= 1
                if i < 0:
                    return 0
            return nums.index(i) + 1
        return nums.index(target)   
        