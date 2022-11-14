class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i,j):
            points.discard((i,j))
            for k in rows[i]:
                if (i, k) in points:
                    dfs(i,k)
            for l in cols[j]:
                if (l, j) in points:
                    dfs(l,j)
            
        points, island, rows, cols = {(i,j) for i, j in stones}, 0, collections.defaultdict(list), collections.defaultdict(list)
        
        for i,j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i,j in stones:
            if (i,j) in points:
                dfs(i,j)
                island += 1
        return len(stones) - island
        
        
        
        #for i in range(len(stones)):
        #    if stones[i][0] == stones[i+1][0]:
        #        del stones[i][0]
        #    for j in range(len(stones)):
        #        if stones[j][1] == stones[j+1][1]:
        #            del stones[j][1]
