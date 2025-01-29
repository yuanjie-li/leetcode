class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s = list(s)
        output = 0
        max_len = len(s)

        # O(n^2) solution 
        for i in range(max_len):
            for j in range(i+1, max_len+1):
                
                sub_str = len(s[i:j])
                set_str = len(list(set(s[i:j])))

                # No dups, then save  
                if set_str == sub_str:
                    if sub_str > output:
                        output = sub_str
                # At first dup, all subsequent sub_str will have dups
                else:
                    break

        return output 
