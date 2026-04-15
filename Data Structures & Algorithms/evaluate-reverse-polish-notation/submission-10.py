class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '-' or token == '+' or token == '/'or token == '*':
                stack.append(int(self.getResult(stack, token)))
            else:
                stack.append(int(token))

        return stack.pop()
    
    def getResult(self, stack, token):
        o1 = int(stack.pop())
        o2 = int(stack.pop())

        if token == '-':
            return o2 - o1
        elif token == '+':
            return o2 + o1
        elif token == '*':
            return o2 * o1
        else:
            return o2 / o1
