class Solution:
    def longestPalindrome(self, s: str) -> str:
        visted_chars = {}
        longest_palindrome = s[0]
        for index, char in enumerate(s):
            if char not in visted_chars:
                visted_chars[char] = [index]
            else:
                for visted_char in visted_chars[char]:
                    sub_str = s[visted_char : index + 1]
                    if len(sub_str) > len(longest_palindrome):
                        if sub_str == sub_str[::-1]:
                            longest_palindrome = sub_str
                    else:
                        continue
                visted_chars[char].append(index)
        return longest_palindrome

                
        