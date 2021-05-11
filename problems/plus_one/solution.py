class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, -1 , -1):
            curr = digits[i]
            if curr != 10:
                break
            else:
                digits[i] = 0
                if i != 0:
                    digits[i - 1] += 1
                else:
                    digits.insert(0, 1)
        return digits
        