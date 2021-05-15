class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        mult = 1
        if s[0] == '-':
            mult = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        ret = ""
        for char in s:
            if not char.isdigit():
                break
            ret += char
        return 0 if ret == "" else min(2 ** 31 - 1, max(int(ret) * mult, -2 ** 31))            
        