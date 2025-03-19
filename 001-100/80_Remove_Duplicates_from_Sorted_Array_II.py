class Solution:
    
    def removeElem(self, l, idx) -> list: 
        ''' Remove element from idx, fill end with None '''

        for i in range(idx, len(l) - 1):
            l[i] = l[i+1]
        l[-1] = None 
        return l 
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Base case where dups are impossible
        if len(nums) < 3: 
            return len(nums)

        cur_idx = 2
        k = 3 

        while cur_idx < len(nums): 
            trip_elem = nums[cur_idx-2]
            cur_elem = nums[cur_idx]
            
            if cur_elem is None: 
                break 

            if trip_elem == cur_elem: 
                nums = self.removeElem(nums, cur_idx)
            else: 
                cur_idx += 1 
                k += 1 

        # k takes one more step than needed.
        return k - 1 
