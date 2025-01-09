class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = { ")": "(", "]": "[", "}": "{"}
        result = list()

        for i in range (len(s)):
            if s[i] in match.values():
                result.append(s[i])
            elif not result or match[s[i]] != result.pop():
                return False

        return result == []