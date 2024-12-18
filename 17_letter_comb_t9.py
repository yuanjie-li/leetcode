class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
            
        t9 = {
            '1':[]
            ,'2':['a','b','c']
            ,'3':['d','e','f']
            ,'4':['g','h','i']
            ,'5':['j','k','l']
            ,'6':['m','n','o']
            ,'7':['p','q','r','s']
            ,'8':['t','u','v']
            ,'9':['w','x','y','z']
            ,'0':[' ']
        }

        output = [''] 
        for digit in digits: 
            
            letters = t9[digit]
            new_output = []
            for sub_output in output:
                for letter in letters:
                    new_output.append(sub_output + letter)
            output = new_output 
        return output 
