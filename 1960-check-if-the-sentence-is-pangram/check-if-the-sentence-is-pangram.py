class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        count = set()
        for letter in sentence:
            count.add(letter)
            if len(count) >= 26:
                return True
        return False
        