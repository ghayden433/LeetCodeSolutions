class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for token in tokens:
            if token[-1].isdigit():
                stack.append(token)
            else:
                opTwo = stack.pop()
                opOne = stack.pop()
                stack.append(str(int(eval(opOne + token + opTwo))))

        return int(stack.pop())
                
