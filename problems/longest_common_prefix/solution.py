class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        max_prefix = ""

        for i in range(min([len(x) for x in strs])):
            curr_char = strs[0][i]
            for x in range(1, len(strs)):
                if strs[x][i] != curr_char:
                    return strs[0][:i]
                else:
                    max_prefix = strs[0][:i + 1]
        return max_prefix