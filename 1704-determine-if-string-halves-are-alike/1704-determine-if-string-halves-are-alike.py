class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, 0
        half = len(s) // 2
        
        for l, r in zip(s[:half], s[half:]):
            if l in vowels: left += 1 
            if r in vowels: right += 1
        
        return left == right