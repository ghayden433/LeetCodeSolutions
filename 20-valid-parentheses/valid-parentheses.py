class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def find(list, item):
            for i in range(len(list)):
                if list[i] == item:
                    return i
            return -1; 

        result = [""]
        paraOpen = ["(", "[", "{"]
        paraClose = [")", "]", "}"]

        for i in range (len(s)):
            if s[i] in paraOpen:
                result.append(s[i])
            elif find(paraClose, s[i]) == find(paraOpen, result[len(result) - 1]):
                result.pop(len(result) - 1)
            else:
                result.append(s[i])
            
        return result == [""]