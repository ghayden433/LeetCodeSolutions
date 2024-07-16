class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        for item in strs:
            key = (''.join(sorted(item)))
            result[key].append(item)
        return result.values()

        