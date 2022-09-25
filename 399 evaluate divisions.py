import numpy as np

class Solution:            
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # get the set of all variables present in the equations
        allVariables = set()
        for eq in equations:
            allVariables.add(eq[0])
            allVariables.add(eq[1])
        variables = list(allVariables)
        # build a dict to lookup vector and matrix indices of a given variable
        var2ind = dict()
        for i, var in enumerate(variables):
            var2ind[var] = i
        nVar = len(variables)
        nEq  = len(equations)
        # bulid matrix M with coefficients from the equations
        M = np.zeros((nEq, nVar))
        ret = []
        for i in range(nEq):
            M[i, var2ind[equations[i][1]]] = values[i]
            M[i, var2ind[equations[i][0]]] = -1
        ret = []
        ### the main loop over queries
        for a, b in queries:
            # special case: query for a variable which is not in the equations
            if not (a in var2ind) or not (b in var2ind):
                ret.append(-1.0)
                continue
            # special case: both variables are equal. return 1.
            if a == b:
                ret.append(1.0)
                continue
            ind = var2ind[b]    # index of the second variable
            yq = -M[: , ind]    # yq becomes minus the column corresponding to b
            Mq = np.delete(M, ind, 1)  # and this column is removed from M
            u, S, vt = np.linalg.svd(Mq, full_matrices=False)  # SVD decomposition of Mq
            indA = var2ind[a]  # what is the index of the first variable?
            if indA > ind: # in case indA is after ind(b) we need to correct for the removal of b
                indA -= 1
            # the actual computation of the solution:
            # Y=M*x => Y=(u*S*vt)x => (u*S*vt)^-1*Y=x => ut*(1/S)*v*y is the solution for x.
            solution = (np.transpose(vt) @ np.diag(S/(S**2+0.0000000000001)) @ np.transpose(u) @ yq)[indA]
            if abs(solution) < 1e-10:  # this regression assigns smallest norm solution
                # so if there is no depencende of a vs b, then 0 is returned. We need to output -1 instead
                solution = -1
            ret.append(solution)
        return ret
