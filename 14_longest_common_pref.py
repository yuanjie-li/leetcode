class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ''
        for idx, char in enumerate(strs[0]):
            
            for s in strs: 
                if idx >= len(s) or char != s[idx]:
                    return prefix 
            
            prefix += char

        return prefix 
            
