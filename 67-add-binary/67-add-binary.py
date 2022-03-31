class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, result, a, b = 0, '', list(a), list(b)
        
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            result += str(carry%2)
            carry //= 2
            
        return result[::-1]