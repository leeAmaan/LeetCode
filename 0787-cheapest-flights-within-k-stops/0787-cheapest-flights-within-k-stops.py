class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        INF=float('inf')
        mn=[INF]*n
        mn[src]=0
        
        for k in range(K+1):
            newmn=mn[:]
            for (a,b, cost) in flights:
                newmn[b]=min(newmn[b],mn[a]+cost)
            mn=newmn
            
        return mn[dst] if mn[dst]!=INF else -1