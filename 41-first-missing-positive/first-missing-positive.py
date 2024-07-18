class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = set()
        for item in nums:
            result.add(item)
        
        i = 1
        while True:
            if i not in result:
                return i
            i += 1
        