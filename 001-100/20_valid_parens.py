class Solution:
    def isValid(self, s: str) -> bool:
        
        open_brac = ['(','{','[']
        close_brac = {
            ')':'('
            ,'}':'{'
            ,']':'['
        }

        if len(s) == 0: return True 
        if len(s) == 1: return False 

        char_stack = []
        for char in s:
            if char in close_brac.keys(): 
                if len(char_stack) == 0 or char_stack[-1] != close_brac[char]:
                    return False 
                else: 
                    char_stack.pop() 
            elif char in open_brac: 
                char_stack.append(char)

        if len(char_stack) > 0: 
            return False             
        return True
