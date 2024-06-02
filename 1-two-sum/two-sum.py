class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range (len(nums)):
            if nums[i] in hashmap:
                return[i, hashmap[nums[i]]]
            else:
                hashmap[target - nums[i]] = i 