class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_ = 0
        for i in s.strip()[::-1]:
            if i == " ":
                return len_
            len_ += 1 
        return len_
        