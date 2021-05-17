class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triange = []
        for i in range(numRows):
            triange.append([math.comb(i, x) for x in range(i + 1)])
        return triange

        