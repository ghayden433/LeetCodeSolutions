class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = ""
        for letter in s:
            if letter.isalnum():
                s2 = s2 + letter.lower()

        left = 0
        right = len(s2) - 1
        while left <= right:
            if s2[left] == s2[right]:
                left+= 1
                right-= 1
            else:
                return False
        return True