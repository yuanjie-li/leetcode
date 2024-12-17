class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        max_water = 0 
        pt1 = 0 
        pt2 = len(height) - 1 

        while pt1 != pt2: 
            cur_water = (pt2 - pt1) * min(height[pt1], height[pt2])

            if cur_water > max_water: 
                max_water = cur_water 
            
            if height[pt1] < height[pt2]: 
                pt1 += 1
            else:
                pt2 -= 1

        return max_water
