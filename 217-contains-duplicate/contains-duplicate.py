class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupe = set()
        for num in nums:
            if num in dupe:
                return True
            dupe.add(num)

        return False

        