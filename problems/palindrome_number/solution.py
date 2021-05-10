class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_ = str(x)
        return str_ == str_[::-1]