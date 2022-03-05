class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        se = 0
        for i in range(0, len(s)-1):
            if Roman[s[i]] < Roman[s[i+1]]:
                se -= Roman[s[i]]
            else:
                se += Roman[s[i]]
                
        return se + Roman[s[-1]]
        