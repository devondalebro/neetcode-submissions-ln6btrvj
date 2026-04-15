from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.listPars = []
        self.addPar("", n, 0, 0)
        return self.listPars

    def addPar(self, current_pars: str, max_pars: int, open_count: int, close_count: int):
        if len(current_pars) == 2 * max_pars:
            self.listPars.append(current_pars)
            return

        if open_count < max_pars:
            self.addPar(current_pars + "(", max_pars, open_count + 1, close_count)

        if close_count < open_count:
            self.addPar(current_pars + ")", max_pars, open_count, close_count + 1)