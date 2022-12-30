class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(formed):
            if formed[-1] == n-1:
                ans.append(formed)
                return
            for child in graph[formed[-1]]:
                dfs(formed + [child])
        
        ans = []
        n = len(graph)
        dfs([0])
        return ans
        
        
        
        
        
        
        """def SorceTarget(graph):
            
        for i in range():
            graph[0][i]
            
            
            
        return SorceTarget(graph)"""