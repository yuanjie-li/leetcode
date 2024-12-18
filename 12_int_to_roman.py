class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return '' 

        roman_dict = {
            1 : {
                1: 'I'
                ,5: 'V'
            }
            ,10 : {
                1: 'X'
                ,5: 'L'
            }
            ,100 : {
                1: 'C'
                ,5: 'D'
            }
            ,1000 : {
                1: 'M'
            }
        }

        output = ''

        for dec in [1000, 100, 10, 1]:
            digit = num % (10 * dec) // dec 
            
            # 9 is special case 
            if digit == 9: 
                output += roman_dict[dec][1]
                output += roman_dict[dec * 10][1]

            elif digit > 4: 
                output += roman_dict[dec][5]
                output += roman_dict[dec][1] * (digit - 5)
            
            # 4 is special case 
            elif digit == 4:
                output += roman_dict[dec][1]    
                output += roman_dict[dec][5]
            else:
                output += roman_dict[dec][1] * digit
             

        return output
