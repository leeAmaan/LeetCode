class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0 
        
        for i in range(len(digits)):
            result += digits[i]*pow(10,(len(digits)-1-i))
        return [int(i) for i in str(result+1)]
        