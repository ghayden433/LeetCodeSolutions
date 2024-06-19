class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while(nums.count(val)):
            nums.remove(val)
            i += 1
        return len(nums)