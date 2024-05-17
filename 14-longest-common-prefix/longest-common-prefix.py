class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        least = "0" * 201
        for i in range (len(strs)):
            if len(strs[i]) <= len(least):
                least = strs[i]
        
        for j in range(len(least)):
            for i in range(len(strs)):
                if strs[i][j] != least[j]:
                    return result
            result = result + least[j]

        return result

        