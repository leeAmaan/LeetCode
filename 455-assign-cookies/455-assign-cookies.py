class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 문제에선 정렬되어있다는 가정이 없으므로 정렬 해준다.
        g.sort()
        s.sort()
        
        child_i = cookie_j = 0
        
        # 만족하지 못할 때까지 그리디 진행한다.
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
                
            cookie_j += 1
        
        return child_i
        