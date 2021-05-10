class Solution:
    def isValid(self, s: str) -> bool:
        open_ = []
        for x in s:
            if x in ["[", "{", "("]:
                open_.insert(0, x)
            else:
                if(len(open_) == 0):
                    return False
                j = open_.pop(0)
                if (x == "]" and j != "[") or (x == "}" and j != "{") or (x == ")" and j != "("):
                    return False
        return True if len(open_) == 0 else False


        