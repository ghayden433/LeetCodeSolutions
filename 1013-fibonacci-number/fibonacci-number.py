class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1]
        while len(nums) <= n:
            nums.append(nums[len(nums) - 1] + nums[len(nums) - 2])
        return nums[n]