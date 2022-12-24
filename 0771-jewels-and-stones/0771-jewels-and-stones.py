class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0
        
        # 비교 없이 보석 빈도 수 합산 
        for char in jewels:
            count += freqs[char]
        return count
        #return sum(s in jewels for s in stones)
        
        