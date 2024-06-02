class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()

        resultIterator = 0
        for i in range (len(nums)):
            if (nums[i] > 1):
                break
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                if (total == 0):
                    result.add((nums[i], nums[left], nums[right]))
                    right -= 1
                if (total > 0):
                    right -= 1
                if (total < 0):
                    left += 1

        return list(result)
            


        