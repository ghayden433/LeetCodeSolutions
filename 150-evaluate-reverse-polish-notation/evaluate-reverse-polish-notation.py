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
                if token == "+":
                    stack.append(str(int(int(opOne) + int(opTwo))))
                elif token == '-':
                    stack.append(str(int(int(opOne) - int(opTwo))))
                elif token == "*":
                    stack.append(str(int(int(opOne) * int(opTwo))))
                elif token == "/":
                    stack.append(str(int(int(opOne) / int(opTwo))))

        return int(stack.pop())
                
