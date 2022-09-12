class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res, cur = 0, 0 
        d = collections.deque(sorted(tokens))
        # print(d)
        while d and (d[0] <= power or cur):
            if d[0] <= power:
                power -= d.popleft()
                cur += 1
            else:
                power += d.pop()
                cur -= 1
            res = max(res, cur)
            
        return res
        
        
        
        
        
        
        
        
        # tokens = 
        #if sum(tokens) < sum(power):
        #    res += power
            
        #    return res 
        
        #elif :
        #else:    
        #for i in range()