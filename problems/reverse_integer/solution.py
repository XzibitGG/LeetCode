class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        reverse = int(str(abs(x))[::-1])
        return reverse*sign*(reverse < 0x7FFFFFFF)
        