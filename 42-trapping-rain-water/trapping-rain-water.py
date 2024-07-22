class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0
        left = [0] * len(height)
        right = [0] * len(height)
        final = list()
        lMax = 0
        rMax = 0
        for i in range(len(height)):
            left[i] = lMax
            if height[i] > lMax:
                lMax = height[i]
            
            right[len(right) - i - 1] = rMax
            if height[len(height) - i - 1] > rMax:
                rMax = height[len(height) - i - 1]

        for i in range(len(height)): 
            hold = min(left[i], right[i]) - height[i]
            if hold > 0:
                total += hold
                
        return total
        