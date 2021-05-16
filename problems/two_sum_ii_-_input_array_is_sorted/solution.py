class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = {}
        for i , j in enumerate(numbers):
            if target - j in x:
                return [x[target - j], i + 1]
            else:
                x[j] = i + 1

