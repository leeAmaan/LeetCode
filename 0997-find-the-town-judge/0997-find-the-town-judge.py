class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        cands = [0] * (n+1)
        for elem1, elem2 in trust:
            cands[elem2] += 1
            cands[elem1] -= 1
        #print(cands)
        return cands.index(n-1) if n-1 in cands else -1
         
        """
        a = trust[0][1]
         
        if trust[a-1][1] is None:
            return trust[0][1]
        elif a != trust[a-1][1]:
            return -1
        else:
            return trust[0][1]"""