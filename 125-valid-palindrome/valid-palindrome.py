class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            #skip over the non alphanumeric chars
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
    
            if s[left].lower() == s[right].lower():
                left+= 1
                right-= 1
            else:
                return False
        return True