class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
            
        route = []
        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
        
        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]
## 이 처럼 그래프를 역순으로 구성하면 추출 시에 pop()으로 처리가 가능하다. 이렇게 하면 복잡도를 
## O(1)로 개선할 수 있다. 만일 크기가 크면 pop()과 pop(0)의 성능 차이는 O(1)과 O(n)으로 차이가 날 수있으므로
## 주의가 꽤나 필요하다.