class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return {}
        result = list() 
        pointers = [0] * len(digits)  
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        while pointers[0] < len(letters[int(digits[0])]):
            temp = ""
            for i in range(len(digits)):
                temp = temp + letters[int(digits[i])][pointers[i]]
            result.append(temp)
            pointers[len(pointers) - 1] += 1
            for i in range(len(pointers) - 1, 0, -1):
                if pointers[i] >= len(letters[int(digits[i])]):
                    pointers[i - 1] += 1
                    pointers[i] = 0
        return result