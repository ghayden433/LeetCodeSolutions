class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1] * (len(nums))
        suffix = [1] * (len(nums))

        total = 1
        for i in range(len(nums) - 1):
            total = total * nums[i]
            prefix[i + 1] = total
        
        total = 1
        for i in range(len(nums) - 1, 0, -1):
            total = total * nums[i]
            suffix[i - 1] = total

        product = [0] * len(nums)
        for i in range(len(nums)):
            product[i] = prefix[i] * suffix[i]
        
        return product
        