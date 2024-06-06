class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = { "(": ")", "[": "]", "{": "}"}
        result = [""]

        for i in range (len(s)):
            if s[i] in match.keys():
                result.append(match[s[i]])
            elif s[i] == result[-1]:
                result.pop()
            else:
                return False
            
        return result == [""]