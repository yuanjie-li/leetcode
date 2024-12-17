import math 
class Solution:
    def reverse(self, x: int) -> int:
         
        (is_neg := x < 0)
        x = abs(x) 
        x = int(str(x)[::-1])


        if x > math.pow(2,31) - 1 or x < -1 * math.pow(2,31):
            return 0
        if is_neg: 
            return -1 * x
        return x 
        
