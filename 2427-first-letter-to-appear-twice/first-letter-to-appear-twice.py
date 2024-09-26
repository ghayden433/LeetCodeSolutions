class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        found = set()
        for letter in s:
            if letter in found:
                return letter
            found.add(letter)
        