class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(N^2) solution
        for idx1, first in enumerate(nums): 
            new_tar = target - first

            try:
                idx2 = nums[idx1+1:].index(new_tar)
                return [idx1, idx2 + idx1 + 1]
            except:
                continue 
            
