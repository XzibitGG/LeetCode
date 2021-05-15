class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        grid = [[]*numRows for i in range(numRows)]
        i = 0
        step = 1
        for char in s:
            grid[i].append(char)
            i += step
            if i == numRows -1 or i == 0:
                step *= -1
        return "".join(["".join(row) for row in grid])

        