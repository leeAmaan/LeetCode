class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(set)
        
        for s, d, weight in flights:
            graph[s].add((d, weight))
            
        #cost, cur_node, stops_in_path, visited
        heap = [[0,src,0, set()]]
        heapq.heapify(heap)
        memo = set()
        while heap:
            cost, node, stops, visited = heapq.heappop(heap)
            if node == dst:
                return cost
            if node not in graph:
                continue
            if stops > k:
                continue
            if node in visited or (node, stops) in memo:
                continue
            memo.add((node, stops))
            visited.add(node)
            for ney, weight in graph[node]:
                heapq.heappush(heap, [cost + weight, ney, stops + 1, visited.union({node})])
        return -1