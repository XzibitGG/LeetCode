class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_char_index = {}
        max_length = 0
        start_index = 0
    
        for i in range(len(s)):
            if s[i] in last_char_index:
                start_index = max(start_index, last_char_index[s[i]] + 1) 
            max_length = max(max_length, i-start_index + 1)
            last_char_index[s[i]] = i
    
        return max_length
            



        