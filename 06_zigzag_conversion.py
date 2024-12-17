class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) < 2 or numRows == 1: 
            return s
        
        tot_len = len(s)
        output = '' 
        max_skip = 2 * (numRows) - 2

        for row_idx in range(0, numRows):

            # There is a skip patter for looking for the up zig
            skip_up = 2 * (numRows - row_idx) - 2 
            if skip_up == 0:
                skip_up = max_skip
            # Which is mirrored by the down zag 
            skip_down = max_skip - skip_up

            char_idx = row_idx
            last_up = 1

            # Run back and forth, concat if value expected. 
            while char_idx < tot_len: 

                if last_up:
                    if skip_up > 0:
                        output += s[char_idx] 
                        char_idx += skip_up 
                    last_up ^= 1
                else:
                    if skip_down > 0:
                        output += s[char_idx]
                        char_idx += skip_down 
                    last_up ^= 1
        
        return output
        
