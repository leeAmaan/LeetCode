class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set([0])
        
        def dfs(room):
            for neib in rooms[room]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib)
                    
        dfs(0)
        return len(visited) == len(rooms)    