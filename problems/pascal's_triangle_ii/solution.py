class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [math.comb(rowIndex, x) for x in range(rowIndex + 1)]
        