class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = list()
        top = dict()
        for num in nums:
            if top.get(num) is not None:
                top[num] = top[num] + 1
            else:
                top[num] = 1
        result = [(v, h) for h, v in top.items()]
        print(result.sort(reverse = True))
        return(([h[1] for h in result])[:k])
        