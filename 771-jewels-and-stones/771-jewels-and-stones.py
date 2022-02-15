class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0 
        
        # 비교 없이 돌(stones)의 빈도 수 계산
        for char in stones:
            freqs[char] += 1
            
        # 비교 없이 보석(jewels)의 빈도 수 합산
        for char in jewels:
            count += freqs[char]
                
        return count
        
        