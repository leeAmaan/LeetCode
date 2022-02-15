class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones) # 돌 빈도수 계산
        count = 0 
        
        # 비교 없이 보석(jewels)의 빈도 수 합산
        for char in jewels:
            count += freqs[char]
                
        return count
        
        