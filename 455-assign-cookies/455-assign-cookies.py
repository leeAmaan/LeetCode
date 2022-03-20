class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 문제에선 정렬되어있다는 가정이 없으므로 정렬 해준다.
        g.sort()
        s.sort()
        
        result = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
                
                
        return result
            
        