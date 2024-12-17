class Solution:
    def myAtoi(self, s: str) -> int:
        
        sign = None
        output = ''
        leading = True 

        for char in s: 
            if leading and char == ' ':
                continue 
            elif leading:
                if char == '-' and sign is None:
                    sign = -1
                    continue
                    leading = False              
                if char == '+' and sign is None:
                    sign = 1
                    leading = False 
                    continue
                try: 
                    int(char)
                    leading = False  
                except: return 0
            else:
                leading = False 
            
            
            try:
                char = str(int(char))

                # Assume positive                 
                if sign is None:
                    sign = 1

                output += char

            except: 
                break 

        if output == '':
            return 0 
            
        output = sign * int(output)

        if output > math.pow(2,31) - 1:
            return int(math.pow(2,31) - 1)
        if output < -1 * math.pow(2,31):
            return int(-1 * math.pow(2,31))
        return output
            
