class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = set()
        minnum = 2000000000
        for item in nums:
            result.add(item)
            if item < minnum and item > 0:
                minnum = item
        
        if minnum != 1:
            return 1


        i = 1
        while True:
            if i not in result:
                return i
            i += 1
        