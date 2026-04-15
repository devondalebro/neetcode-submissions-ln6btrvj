class Solution:
    def isValid(self, s: str) -> bool:
        par = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                par.append(c)
            elif c == ')':
                if len(par) == 0 or par.pop() != '(':
                    return False
            elif c == '}':
                if len(par) == 0 or par.pop() != '{':
                    return False
            elif c == ']':
                if len(par) == 0 or par.pop() != '[':
                    return False

        return len(par) == 0

        