class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sorteds1 = ''.join(sorted(s1))
        for i in range(len(s2) - len(s1) + 1):
            if s2[i] in s1:
                if ''.join(sorted(s2[i:(i + len(s1))])) == sorteds1:
                    return True
        
        return False
        