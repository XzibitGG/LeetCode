class Solution:
    def mySqrt(self, k: int) -> int:
        x = (k + 1)/4.0
        x2 = x * x
        
        diff = x2 - k
        e = 0.5
        
        while diff < -e or diff > e:
            x = x + (k - x2) / (2 * x)
            x2 = x * x
            diff = x2 - k
        
        return int(x)
        