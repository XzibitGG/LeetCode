class Solution:

    def __init__(self):
        self.symbols = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

    def romanToInt(self, s: str) -> int:
        total = 0
        last = 0
        for i in s[::-1]:
            curr_value = self.symbols[i]
            if last / curr_value in [5, 10]:
                total -= curr_value
            else:
                total += curr_value
            last = curr_value
        return total

        