class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x) 
        tot_len = len(x)

        for i in range(tot_len // 2): 
            if x[i] != x[tot_len-i-1]:
                return False
        return True 
