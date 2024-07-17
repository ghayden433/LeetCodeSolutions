class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxSeq = 0

        for num in nums:
            # if this could be the start of a sequence
            if num-1 not in nums:
                i = 1
                while ((num + i) in nums):
                    i+= 1
                if i > maxSeq:
                    maxSeq = i
        
        return maxSeq

