class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        count = 0
        for num in nums:
            if num == result:
                count += 1
            else:
                count -= 1
                if count < 0:
                    result = num
                    count = 0
        
        return result
        