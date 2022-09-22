class Solution:
    def reverseWords(self, s: str) -> str:
        res = 0 
        print(s[1])
        
        
        
        return ' '.join(s.split()[::-1])[::-1]