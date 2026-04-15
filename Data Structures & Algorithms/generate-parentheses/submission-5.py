class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.listPars = []
        self.addPar("", "(", n, 1)

        return self.listPars

                
    def addPar(self, pars, par, n, nOpen):
        pars += par
        if len(pars) == 2 * n:
            return self.listPars.append(pars)
        
        
        if nOpen < n:
            self.addPar(pars, "(", n, nOpen + 1)

        if nOpen > len(pars) - nOpen:
            self.addPar(pars, ")", n, nOpen)
