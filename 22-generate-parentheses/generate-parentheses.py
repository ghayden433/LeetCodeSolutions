class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        result = list()

        def genPar(s, openPar, closePar):
            if len(s) == n*2:
                result.append(s)
                return
            if openPar < n:
                genPar(s + "(", openPar + 1, closePar)
            if closePar < openPar:
                genPar(s + ")", openPar, closePar + 1)
            return
        genPar("(", 1, 0)
        return result



        return result
