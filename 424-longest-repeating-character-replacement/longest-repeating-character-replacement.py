class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        result = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - (max(count.values())) > k: 
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        return result