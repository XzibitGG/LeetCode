class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return
        phone = {
            "2" : list('abc'),
            "3" : list('def'),
            "4" : list('ghi'),
            "5" : list('jkl'),
            "6" : list('mno'),
            "7" : list('pqrs'),
            "8" : list('tuv'),
            "9" : list('wxyz')
        }
        possible_chars = []
        for i in digits:
            if i != '1':
                possible_chars.append(phone[i])

        return self.find_combinations(possible_chars)

    def find_combinations(self, letters):
        if len(letters) == 1:
            return letters.pop(0)
        else:
            first = letters.pop(0)
            second = letters.pop(0)
            curr_combinations = []
            for i in first:
                for x in second:
                    curr_combinations.append(i + x)
            letters.insert(0, curr_combinations)
            return self.find_combinations(letters)
                