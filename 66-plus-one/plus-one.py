class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def addOne(index):
            if digits[index] == 9:
                digits[index] = 0
                if index == 0:
                    digits.insert(0, 0)
                    addOne(index)
                else:
                    addOne(index - 1)
            else:
                digits[index] += 1
        
        addOne(len(digits) - 1)
        return digits

        