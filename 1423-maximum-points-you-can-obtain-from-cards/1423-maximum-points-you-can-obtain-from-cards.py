class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cardL, cardS = len(cardPoints), sum(cardPoints)
        minSubArraySum = window = sum(cardPoints[:cardL-k])
        for i in range(cardL-k, cardL):
            window = window - cardPoints[i-cardL+k] + cardPoints[i]
            minSubArraySum = min(minSubArraySum, window)
        
        return cardS - minSubArraySum
        
        
        
        
        
        
        
        
        
