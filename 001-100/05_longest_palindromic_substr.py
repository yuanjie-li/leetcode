class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Catch edge cases 
        if len(s) <2:
            return s
        
        def _check_palin(s):

            # Iterate through half of the string
            tot_idx = len(s) - 1  
            for idx in range( tot_idx // 2 + 1 ): 
                if s[idx] != s[tot_idx - idx]: 
                    return False 
            return True 
        
        # Iterate through to make all substrings 
        output = ''
        max_len = 0
        tot_idx = len(s) - 1              
        for i in range(tot_idx):
            # +2 since end is exclusive 
            for j in range(i + 1, tot_idx + 2):

                sub_str = s[i:j]
                if len(sub_str) <= max_len: 
                    continue 
                
                is_palin = _check_palin(sub_str)
                if is_palin and len(sub_str) > max_len:
                    output = sub_str
                    max_len = len(sub_str)

        return output        
