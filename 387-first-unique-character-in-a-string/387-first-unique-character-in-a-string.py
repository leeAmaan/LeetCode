
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(i) for i in letters if s.count(i) == 1]
        return min(index) if len(index) > 0 else -1 
            
            